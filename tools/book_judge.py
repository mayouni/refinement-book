"""How a block is judged against its promise: the site's own judge, copied, not reimplemented.

Lineage (so the book's verdicts mean what the site's mean):
  parse, FORBIDDEN   <- stzsite tools/harvest_examples.py   at stzsite fa8e1e605
  norm, bare, verdict <- stzsite tools/showcase_run.py      at stzsite fa8e1e605
  WORDS              <- stzsite tools/build_narration_pages.py T, at stzsite fa8e1e605
The bodies below are the site's, word for word. What the book adds is marked "book:".
"""
import re

# ---------------------------------------------------------------- from harvest_examples.py
FORBIDDEN = re.compile(r"\b(give|getchar|input|system|SystemCall|write|read|remove|Now|NowXT|Today|TodayXT|Clock|"
                       r"random|rnd\w*|Sleep|sleep|Download|http\w*|FileCreate|FileOverwrite|FileAppend|FileSave|"
                       r"StzFileSave|RemoveFile|DeleteFile|MakeDir|StzMakeDir|stzFolder|stzFile|shell|Exec\w*|"
                       r"ToPNG\w*|ToSVG\w*|Show\w*|Render\w*|Plot\w*|Draw\w*|Display\w*|pf|pr|load)\s*\(", re.I)


def parse(text):
    text = re.sub(r"/\*.*?\*/", "", text.replace("\r", "").lstrip("﻿"), flags=re.S)
    code, promises, in_promise = [], [], False
    for raw in text.split("\n"):
        s = raw.strip()
        if not s:
            in_promise = False; continue
        if s.startswith("#-->"):
            promises.append(s[4:].strip()); in_promise = True; continue
        if s.startswith("#") or s.startswith("//"):
            if in_promise and not s.startswith("# Executed"):
                promises[-1] += "\n" + s.lstrip("#").strip()
            continue
        in_promise = False
        if re.match(r"(?i)(load\s|pr\(\)|pf\(\)|StopProfiler\(\)|pron\(\)|proff\(\))", s):
            continue
        m = re.match(r"(.*?)\s#-->\s*(.*)$", s)
        if m and m.group(1).strip().startswith("?"):
            code.append(m.group(1).rstrip()); promises.append(m.group(2).strip()); in_promise = True; continue
        code.append(raw.rstrip())
    return code, [p for p in promises if p]


# ---------------------------------------------------------------- from showcase_run.py
def norm(s):
    """Compare as the reader would: spacing ignored, and TRUE / FALSE as the 1 / 0 they print as."""
    s = re.sub(r"\s+", " ", (s or "").replace("#-->", "").replace("#--", "").strip()).lower()
    return re.sub(r"\bfalse\b", "0", re.sub(r"\btrue\b", "1", s))


def bare(expected):
    """The promise without the remarks a reader added in brackets, such as '(asserted by the guard)'."""
    return re.sub(r"\s*\((?:[^()]*\b(?:asserted|guard|exact match|each)\b[^()]*)\)", "", expected or "")


def verdict(code, text, expected):
    """True when the run kept its source's promise, False when it did not, None when nothing was promised.
    A snippet that asserts through a guard's helpers (Then, Chk) keeps its promise when every assertion
    printed a pass and none a failure; any other snippet is compared with what its source printed."""
    if re.search(r"\b(Then|Chk|ChkEq)\s*\(", code, re.I):
        passes = len(re.findall(r"(?im)\[PASS\]|\[ok\]|^\s*ok\b", text))
        fails = len(re.findall(r"(?im)\[FAIL\]|^\s*fail\b|^\s*not ok\b", text))
        return passes > 0 and fails == 0
    if not expected:
        return None
    # the same values, whatever the display form: a list printed item by item, or written [ "a", "b" ]
    toks = lambda s: re.findall(r'[^\s\[\]",]+', norm(s))
    return norm(text) == norm(expected) or norm(text) == norm(bare(expected)) or toks(text) == toks(bare(expected))


# ---------------------------------------------------------------- from build_narration_pages.py (T)
WORDS = {
  "fr": {"kept": "exécuté : a affiché ce que ce bloc promet", "ran": "exécuté : ce bloc n'annonce pas de sortie ; voici ce qu'il a affiché", "ran0": "exécuté : ce bloc n'annonce pas de sortie et n'a rien affiché",
         "unprinted": "exécuté : sa promesse est écrite sur une ligne qui n'affiche rien, elle n'a pas pu être vérifiée",
         "differs": "exécuté : a affiché autre chose ; voici ce qu'il a affiché", "raised": "exécuté : a levé une erreur",
         "stopped": "n'a pas fini", "promised": "Sortie promise"},
  "en": {"kept": "ran: printed what this block promises", "ran": "ran: this block states no output; here is what it printed", "ran0": "ran: this block states no output and printed nothing",
         "unprinted": "ran: its promise is written on a line that prints nothing, so it could not be checked",
         "differs": "ran: printed something else; here is what it printed", "raised": "ran: raised an error",
         "stopped": "did not finish", "promised": "Promised output"},
}

# book: the verdicts the site has no words for, because the site keeps such blocks off its pages
WORDS["en"].update({
    "exercise": "not run: an exercise, written for you to run",
    "not-run": "not run: {why}",
    "effects": "this block touches {what}; the output shown was recorded on {d}",
})
WORDS["fr"].update({
    "exercise": "non exécuté : un exercice, écrit pour que vous l'exécutiez",
    "not-run": "non exécuté : {why}",
    "effects": "ce bloc touche {what} ; la sortie montrée a été enregistrée le {d}",
})


# book: what a block touches, named so the page can say it (the site's FORBIDDEN, read by family)
EFFECTS = [
    ("input", r"\b(give|getchar|input)\s*\("),
    ("files", r"\b(write|read|remove|FileCreate|FileOverwrite|FileAppend|FileSave|StzFileSave|RemoveFile|DeleteFile|MakeDir|StzMakeDir|stzFolder|stzFile)\s*\("),
    ("the network", r"\b(Download|http\w*)\s*\("),
    ("the clock", r"\b(Now|NowXT|Today|TodayXT|Clock|Sleep|sleep)\s*\("),
    ("chance", r"\b(random|rnd\w*)\s*\("),
    ("the system", r"\b(system|SystemCall|shell|Exec\w*)\s*\("),
]


def effects_of(code):
    return [name for name, rx in EFFECTS if re.search(rx, code, re.I)]
