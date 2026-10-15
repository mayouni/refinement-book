#!/usr/bin/env python3
"""Run every Haro block of every chapter inside the library, and judge each against its promise.

Modelled on the site's tools/narrations_run.py (stzsite fa8e1e605): a chapter is an argument told
in code, each block building on the ones before it, so each chapter runs in ONE process, its blocks
in order, each in its own try block. A block is judged against the `#-->` lines it carries, by the
site's own judge (book_judge.py). Nothing a block prints is stored in a source file: the verdicts
and outputs go to data/book-run.json, and the page shows them from there.

What differs from the site's runner, and why:
  - the library runs from a snapshot at a named commit (book_common.snapshot), never from its
    working checkout, which other sessions write while the book builds;
  - a block that touches files, input, the network, the clock or chance is still run, inside the
    snapshot, and marked with what it touches, so its page can say the output was recorded on a date;
  - a fence written `haro exercise` is the reader's to run: it is recorded as not run, with that reason;
  - a chapter whose runnable blocks did not all keep their promise fails the run: exit status 1.

    python tools/book_run.py                 # the library at its current HEAD
    python tools/book_run.py --commit <sha>  # the library at a named commit
"""
import os, re, sys, subprocess, shutil
from book_common import (sources, code_blocks, block_hash, snapshot, now, stamp, save_json, ROOT, LIB_REF)
from book_judge import parse, verdict, effects_of


def run_chapter(lib, name, blocks):
    """Run one chapter's runnable blocks in one process; return a record per block, in order."""
    work = lib / "base" / "test" / "_rop_book_run"   # its own folder: the Softanza runner uses _book_run
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    records, runnable = [], []
    for b in blocks:
        code, promises = parse(re.sub(r"(#|//)[ \t]*-->", "#-->", b["text"]))
        rec = {"hash": block_hash(b["text"]), "promise":"\n".join(promises), "effects": effects_of("\n".join(code))}
        if "exercise" in b["flags"]:
            rec.update(verdict="exercise", out="")
        else:
            rec["unprinted"] = sum(1 for l in b["text"].split("\n")
                                   if re.search(r"(#|//)[ \t]*-->", l) and not re.match(r"[ \t]*(\?|#|//)", l))
            runnable.append((len(records), code, rec))
        records.append(rec)
    if not runnable:
        shutil.rmtree(work, ignore_errors=True)
        return records, None
    # the max entry loads base first, then the max layer, as the site's narration runner does
    main_lines, tail = ['load "../../../max/stzMax.ring"', ""], []
    for i, code, _ in runnable:
        # a definition starts at column 0; an anonymous function inside a call may sit on an indented line
        cut = next((j for j, l in enumerate(code) if re.match(r"(?i)(func|class)\s+\w", l)), None)
        body, defs = (code[:cut], code[cut:]) if cut is not None else (code, [])
        tail += defs
        main_lines += [f'? "@@BEGIN {i}"', "try"] + body + ["catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
    script = work / "chapter.ring"
    script.write_text("\n".join(main_lines + [""] + tail) + "\n", encoding="utf-8")
    t0 = now()
    try:
        # the library's door to foreign runtimes starts its script by bare name, which a machine that sets
        # NoDefaultCurrentDirectoryInExePath cannot find; the chapter on the door needs it unset
        env = {k: v for k, v in os.environ.items() if k.lower() != "nodefaultcurrentdirectoryinexepath"}
        p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, env=env,
                           encoding="utf-8", errors="replace", timeout=300)
        out = (p.stdout or "").replace("\r", "")
    except subprocess.TimeoutExpired as e:
        out = (e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")).replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    seconds = round((now() - t0).total_seconds(), 1)
    compiled = "@@BEGIN" in out
    for i, code, rec in runnable:
        m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
        if not compiled:
            rec.update(verdict="not-run", why="the chapter's code does not compile", out=out.strip()[-2000:]); continue
        if not m:
            rec.update(verdict="stopped", out=""); continue
        text_out = m.group(1).rstrip()
        if "@@ERROR" in text_out:
            text_out = text_out.replace("@@ERROR ", "")
            # a refusal the block promises is the block keeping its promise (the site's rule)
            refusal = re.sub(r"(?im)^[ \t]*(raises|error)[ \t]*:?[ \t]*", "", rec["promise"])
            v = "kept" if rec["promise"] and verdict("", text_out, refusal) else "raised"
            if v == "raised" and rec["promise"] and re.sub(r"\s+", " ", refusal).strip().lower()[:40] in re.sub(r"\s+", " ", text_out).lower():
                v = "kept"
        elif rec["promise"]:
            v = "kept" if verdict("\n".join(code), text_out, rec["promise"]) else "differs"
        else:
            v = "unprinted" if rec.get("unprinted") else "ran"
        rec.update(verdict=v, out=text_out)
    return records, {"ran": stamp(t0), "seconds": seconds}


def runtime():
    """Which runtime ran the blocks, read from the runtime itself: the book must say it is not yet Haro."""
    exe = shutil.which("ring") or "ring"
    probe = ROOT / ".cache" / "_runtime_probe.ring"   # in this book's own .cache
    probe.parent.mkdir(exist_ok=True)
    probe.write_text("? version()\n", encoding="utf-8")
    try:
        v = subprocess.run([exe, probe.name], cwd=probe.parent, capture_output=True, text=True, timeout=30).stdout.strip()
    finally:
        probe.unlink(missing_ok=True)
    return {"name": "Ring", "version": v or None, "path": exe.replace("\\", "/")}


def main():
    commit = sys.argv[sys.argv.index("--commit") + 1] if "--commit" in sys.argv else LIB_REF
    lib, prov = snapshot(commit)
    started = now()
    result = {"run": {"date": stamp(started), "library": prov, "runtime": runtime()}, "chapters": {}}
    failed = []
    en_by_id = {}
    for lang in ("en", "fr"):
        for path, meta, body in sources(lang):
            key = f"{lang}/{path.stem}"
            blocks = code_blocks(body)
            twin = en_by_id.get(meta["id"]) if lang == "fr" else None
            if twin and [b["hash"] for b in twin["blocks"]] == [block_hash(b["text"]) for b in blocks]:
                # the French page carries the same code as the English one: it is the same run, not a second one
                result["chapters"][key] = {**twin}
                print(f"{key}: the English run, same code ({twin['kept']} of {twin['runnable']} kept)", flush=True)
                continue
            records, timing = run_chapter(lib, key, blocks)
            runnable = [r for r in records if r["verdict"] != "exercise"]
            kept = sum(1 for r in runnable if r["verdict"] == "kept")
            ch = {"id": meta["id"], "blocks": records, "kept": kept, "runnable": len(runnable),
                  "exercises": len(records) - len(runnable)}
            if timing:
                ch.update(timing)
            result["chapters"][key] = ch
            if lang == "en":
                en_by_id[meta["id"]] = ch
            line = f"{key}: {kept} of {len(runnable)} blocks kept their promise"
            if len(runnable) and kept < len(runnable):
                failed.append(key)
                line += "  <- FAILS: " + ", ".join(sorted({r['verdict'] for r in runnable if r['verdict'] != 'kept'}))
            print(line, flush=True)
    result["run"]["failed"] = failed
    save_json("book-run.json", result)
    print(f"library at {prov['short']} ({prov.get('ref', '')}); engine binaries copied, newest built "
          f"{prov['engine_binaries']['newest_build']} -> data/book-run.json")
    if failed:
        print(f"FAILED: {len(failed)} chapter(s) did not keep all their promises")
        sys.exit(1)


if __name__ == "__main__":
    main()
