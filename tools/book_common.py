"""Copied from the Softanza book's tools (softanza-book 0626246) for the Refinement book (ROP-11).

What the book's three tools share: the sources, their code blocks, and the library they run in.

The library is never run in its working checkout: other sessions write that tree while the book
builds, so a run there would be a run at no commit at all. The runner exports the library's files
at a named commit into .cache/ (git archive, which reads the library's history and writes nothing
in its repository) and runs there. The engine binaries are build products, absent from any commit;
they are copied from the working checkout and their build time is recorded beside the run, so the
proof line can say what it cannot pin.
"""
import hashlib, json, re, shutil, subprocess, pathlib, datetime
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DATA = ROOT / "data"
CACHE = ROOT / ".cache"
# the Softanza book exports the same pin (ROP-07); its snapshot is read, never written, when present (228 MB not copied twice)
SHARED_CACHE = ROOT.parent / "softanza-book" / ".cache"
LIB_REPO = pathlib.Path("D:/GitHub/stzlib")          # the library's repository, read only
LIB_IN_REPO = "libraries/stzlib"
# The commit of the library the book runs at, named in full: a branch name moves under the book. It moved on
# 2026-10-08 (five fix branches merged into origin/main, 21:34 to 21:43) and every chapter failed to load until
# the pin was a commit. This one is origin/main as the book's first drafts saw it (2026-10-05 21:50); the
# working checkout was then on a side branch, which is not the library a reader can fetch. Move the pin
# deliberately, then re-run: `python tools/book_run.py --commit <sha>` shows what a newer commit does first.
LIB_REF = "93d7a39bdd040f82eae21d949460d69c32a75c70"
GH_BLOB = "https://github.com/mayouni/stzlib/blob/{sha}/libraries/stzlib/{path}"

FENCE = re.compile(r"(?ms)^```([^\n]*)\n(.*?)^```[ \t]*$")
CODE_TAG = "haro"                                     # the language's name, as section 4.8 rules


def now():
    """One reading of the clock, never composed."""
    return datetime.datetime.now().astimezone()


def stamp(t):
    """A clock reading as the book prints it: date, minute and the offset from UTC."""
    z = t.strftime("%z")
    return t.strftime("%Y-%m-%d %H:%M ") + "UTC" + (z[:3] + ":" + z[3:] if z else "")


def read_source(path):
    """Front matter (a dict) and body (Markdown) of one chapter file."""
    text = path.read_text(encoding="utf-8").replace("\r", "")
    if not text.startswith("---\n"):
        raise SystemExit(f"{path}: no front matter")
    _, fm, body = text.split("---\n", 2)
    meta = yaml.safe_load(fm) or {}
    for key in ("id", "number", "title", "status"):
        if key not in meta:
            raise SystemExit(f"{path}: front matter has no '{key}'")
    return meta, body.lstrip("\n")


def sources(lang):
    """The chapter files of one language, in book order."""
    d = SRC / lang
    if not d.exists():
        return []
    out = [(p, *read_source(p)) for p in sorted(d.glob("*.md"))]
    return sorted(out, key=lambda r: r[1]["number"])


def structure():
    return yaml.safe_load((SRC / "structure.yaml").read_text(encoding="utf-8"))


def block_hash(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def code_blocks(body):
    """Every Haro fence of a chapter, in order: its info string, its text, and its position."""
    out = []
    for m in FENCE.finditer(body):
        info = m.group(1).strip().split()
        if info and info[0].lower() == CODE_TAG:
            out.append({"flags": [w.lower() for w in info[1:]], "text": m.group(2).rstrip("\n"),
                        "start": m.start(), "end": m.end()})
    return out


def former_name_fences(body):
    """Fences still tagged with the former host language's name: the build refuses them (section 4.8)."""
    return [m.group(1) for m in FENCE.finditer(body) if m.group(1).strip().lower().startswith("ring")]


# --------------------------------------------------------------------------- the library, pinned

def git(*args):
    return subprocess.run(["git", "-C", str(LIB_REPO), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", check=True).stdout.strip()


def snapshot(commit=None):
    """The library's files at one commit, exported once into .cache/, with the engine binaries beside them.
    Returns (path to libraries/stzlib in the snapshot, provenance dict)."""
    sha = git("rev-parse", commit or LIB_REF)
    short = sha[:9]
    base = CACHE / f"stzlib-{short}"
    shared = SHARED_CACHE / f"stzlib-{short}"
    if not (base / LIB_IN_REPO / "base" / "stzBase.ring").exists() and (shared / "provenance.json").exists():
        return shared / LIB_IN_REPO, json.loads((shared / "provenance.json").read_text(encoding="utf-8"))
    lib = base / LIB_IN_REPO
    prov_file = base / "provenance.json"
    if not (lib / "base" / "stzBase.ring").exists():
        base.mkdir(parents=True, exist_ok=True)
        archive = subprocess.Popen(["git", "-C", str(LIB_REPO), "archive", sha, LIB_IN_REPO], stdout=subprocess.PIPE)
        subprocess.run(["tar", "-x", "-C", str(base)], stdin=archive.stdout, check=True)
        archive.wait()
    bin_dst = lib / "engine" / "zig-out" / "bin"
    if not prov_file.exists() or not any(bin_dst.glob("*.dll")):
        tree = engine_tree(sha)
        bin_src = tree / LIB_IN_REPO / "engine" / "zig-out" / "bin"
        bin_dst.mkdir(parents=True, exist_ok=True)
        dlls = sorted(bin_src.glob("*.dll"))
        for f in dlls:
            shutil.copy2(f, bin_dst / f.name)
        newest = max((f.stat().st_mtime for f in dlls), default=None)
        tree_head = subprocess.run(["git", "-C", str(tree), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        # engine sources committed after the binaries were built: the gap the proof line must admit
        later = []
        if newest:
            since = datetime.datetime.fromtimestamp(newest).astimezone().isoformat()
            later = [l for l in git("log", f"--since={since}", "--format=%h %ci %s", sha, "--",
                                    f"{LIB_IN_REPO}/engine/src", f"{LIB_IN_REPO}/engine/build.zig").split("\n") if l]
        prov = {
            "commit": sha, "short": short,
            "ref": commit or LIB_REF,
            "commit_date": git("show", "-s", "--format=%ci", sha),
            "exported": stamp(now()),
            "engine_binaries": {
                "count": len(dlls),
                "copied_from": str(bin_src).replace("\\", "/"),
                "built_in_a_tree_at_this_commit": tree_head == sha,
                "newest_build": (stamp(datetime.datetime.fromtimestamp(newest).astimezone()) if newest else None),
                "engine_commits_after_build": later,
                "pinned": tree_head == sha and not later,
                "why": "build products are in no commit; a pinned engine build was not run (the machine's build-load rule)",
            },
        }
        prov_file.write_text(json.dumps(prov, indent=1), encoding="utf-8")
    return lib, json.loads(prov_file.read_text(encoding="utf-8"))


def engine_tree(sha):
    """The checkout whose engine build is closest to the commit: a worktree of the library at that exact commit
    (the estate keeps several beside the repository, D:/GitHub/_wt*), else the library's own checkout."""
    for tree in sorted(LIB_REPO.parent.glob("_wt*")) + [LIB_REPO]:
        if not (tree / LIB_IN_REPO / "engine" / "zig-out" / "bin").is_dir():
            continue
        head = subprocess.run(["git", "-C", str(tree), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        if head == sha:
            return tree
    return LIB_REPO


def load_json(name, default):
    p = DATA / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def save_json(name, obj):
    DATA.mkdir(exist_ok=True)
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
