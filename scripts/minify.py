#!/usr/bin/env python3
"""Minify src/engine.py -> src/engine.min.py for the 4 KiB entry cap.

Deterministic, token-based:
  - drops comments and blank lines
  - renames every module-defined name (functions, classes, globals,
    arguments, locals, methods, self.* attributes) to a short name
  - collapses indentation to one space per level
  - never touches string contents, builtins, imported module names or
    attributes of external objects (only attributes that are methods or
    self.* attributes of this module's own classes are renamed)
Run: python3 scripts/minify.py  (reads src/engine.py, writes src/engine.min.py)
"""
import ast
import io
import keyword
import sys
import tokenize

SRC = "src/engine.py"
OUT = "src/engine.min.py"

BUILTINS = set(dir(__builtins__)) | {"self", "cls"}
KEEP = {"__init__", "__repr__", "__str__", "__len__", "__eq__", "__hash__"}

POOL = []
for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    POOL.append(c)
for a in "abcdefghijklmnopqrstuvwxyz":
    for b in "abcdefghijklmnopqrstuvwxyz":
        POOL.append(a + b)
# a short name must itself be a legal, non-keyword, non-builtin identifier
POOL = [p for p in POOL if p not in keyword.kwlist and p not in BUILTINS]


def collect(tree):
    """defined: names to rename as plain tokens.
    attrs: attribute names of this module's own classes (rename after '.').
    Keyword-argument names in calls (e.g. sort(key=...)) are never renamed:
    they are part of the callee's interface, not this module's names."""
    defined = set()
    attrs = set()
    kwargs = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.name not in KEEP:
                defined.add(node.name)
                attrs.add(node.name)  # methods are also attribute names
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            defined.add(node.id)
        elif isinstance(node, ast.arg):
            defined.add(node.arg)
        elif isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name) and node.value.id == "self":
                if node.attr not in KEEP:
                    defined.add(node.attr)
                    attrs.add(node.attr)
        elif isinstance(node, ast.keyword):
            if node.arg:
                kwargs.add(node.arg)
    defined = {n for n in defined if n not in keyword.kwlist and n not in BUILTINS} - kwargs
    attrs = {n for n in attrs if n not in keyword.kwlist and n not in BUILTINS} - kwargs
    return defined, attrs


def main():
    src = open(SRC).read()
    tree = ast.parse(src)
    defined, attrs = collect(tree)
    mapping = {}
    it = iter(POOL)
    for name in sorted(defined, key=lambda n: (-len(n), n)):
        short = next(it)
        while short in defined or short in mapping.values():
            short = next(it)
        mapping[name] = short
    print(f"renaming {len(mapping)} names ({len(attrs)} attrs)", file=sys.stderr)

    tokens = list(tokenize.generate_tokens(io.StringIO(src).readline))
    # Minimal-spacing re-emit: a space only where two adjacent tokens
    # would otherwise merge (both sides start/end with a word character).
    def wordy(s):
        return bool(s) and (s[-1].isalnum() or s[-1] == "_")

    def starts_wordy(s):
        return bool(s) and (s[0].isalnum() or s[0] == "_")

    parts = []
    level = 0
    prev = ""
    prev_sig = None
    at_line_start = True
    for tok in tokens:
        ttype, tstr = tok.type, tok.string
        if ttype == tokenize.COMMENT:
            continue
        if ttype == tokenize.INDENT:
            level += 1
            continue
        if ttype == tokenize.DEDENT:
            level -= 1
            continue
        if ttype in (tokenize.NL, tokenize.NEWLINE):
            if ttype == tokenize.NEWLINE:
                parts.append("\n")
                at_line_start = True
                prev = ""
            continue
        if ttype == tokenize.ENDMARKER:
            continue
        if ttype == tokenize.NAME:
            if prev_sig and prev_sig.string == ".":
                if tstr in attrs:
                    tstr = mapping[tstr]
            elif tstr in mapping:
                tstr = mapping[tstr]
        if at_line_start:
            parts.append(" " * level)
            at_line_start = False
        elif wordy(prev) and starts_wordy(tstr):
            parts.append(" ")
        parts.append(tstr)
        prev = tstr
        if ttype not in (tokenize.NL, tokenize.COMMENT, tokenize.INDENT, tokenize.DEDENT):
            prev_sig = tok
    text = "".join(parts)
    # drop lines left empty by removed comments (indent is already 1 space/level)
    lines = [ln for ln in text.split("\n") if ln.strip()]
    open(OUT, "w").write("\n".join(lines) + "\n")
    print(f"{SRC}: {len(src)} bytes -> {OUT}: {len(open(OUT).read())} bytes", file=sys.stderr)


if __name__ == "__main__":
    main()
