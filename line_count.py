#!/usr/bin/env python3
"""Line counter — wc-like tool with language detection."""
import sys, os
LANG_EXT = {".py":"Python",".js":"JavaScript",".ts":"TypeScript",".go":"Go",".rs":"Rust",".c":"C",".cpp":"C++",".java":"Java",".rb":"Ruby",".sh":"Shell",".md":"Markdown",".html":"HTML",".css":"CSS",".json":"JSON",".yaml":"YAML",".toml":"TOML"}
def count_file(path):
    try:
        with open(path, "r", errors="ignore") as f: content = f.read()
        lines = content.count("\n") + (1 if content and not content.endswith("\n") else 0)
        return lines, len(content.split()), len(content)
    except: return 0, 0, 0
def cli():
    if len(sys.argv) < 2: print("Usage: line_count <file|dir> [--by-lang]"); sys.exit(1)
    target = sys.argv[1]; by_lang = "--by-lang" in sys.argv
    if os.path.isfile(target):
        l, w, c = count_file(target); print(f"  {l:>8} lines  {w:>8} words  {c:>8} chars  {target}")
    elif os.path.isdir(target):
        totals = {}; tl = tw = tc = 0
        for root, _, files in os.walk(target):
            for f in files:
                ext = os.path.splitext(f)[1]; path = os.path.join(root, f)
                l, w, c = count_file(path); tl += l; tw += w; tc += c
                lang = LANG_EXT.get(ext, ext or "other")
                totals[lang] = totals.get(lang, 0) + l
        if by_lang:
            for lang, lines in sorted(totals.items(), key=lambda x: -x[1]): print(f"  {lines:>8}  {lang}")
        print(f"  {tl:>8} lines  {tw:>8} words  {tc:>8} chars  TOTAL")
if __name__ == "__main__": cli()
