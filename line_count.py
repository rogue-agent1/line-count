#!/usr/bin/env python3
"""line_count - Count lines of code by language."""
import sys,os
LANGS={".py":"Python",".js":"JavaScript",".ts":"TypeScript",".go":"Go",".rs":"Rust",
       ".c":"C",".h":"C Header",".cpp":"C++",".java":"Java",".rb":"Ruby",".sh":"Shell",
       ".html":"HTML",".css":"CSS",".sql":"SQL",".md":"Markdown",".json":"JSON",".yaml":"YAML",".yml":"YAML",
       ".toml":"TOML",".xml":"XML",".swift":"Swift",".kt":"Kotlin",".r":"R",".lua":"Lua",".zig":"Zig"}
SKIP={".git","node_modules","__pycache__",".venv","venv","dist","build",".next","target"}
def count(path):
    stats={};
    for root,dirs,files in os.walk(path):
        dirs[:]=[d for d in dirs if d not in SKIP]
        for f in files:
            ext=os.path.splitext(f)[1].lower()
            if ext not in LANGS:continue
            lang=LANGS[ext];fp=os.path.join(root,f)
            try:
                with open(fp,"r",errors="ignore") as fh:
                    lines=fh.readlines();total=len(lines);blank=sum(1 for l in lines if not l.strip())
                    code=total-blank
                stats.setdefault(lang,[0,0,0]);stats[lang][0]+=1;stats[lang][1]+=total;stats[lang][2]+=code
            except:pass
    return stats
if __name__=="__main__":
    path=sys.argv[1] if len(sys.argv)>1 else "."
    stats=count(path);total_f=total_l=total_c=0
    print(f"{'Language':<15} {'Files':>6} {'Lines':>8} {'Code':>8} {'Blank':>8}")
    print("-"*50)
    for lang in sorted(stats,key=lambda l:-stats[l][1]):
        f,l,c=stats[lang];total_f+=f;total_l+=l;total_c+=c
        print(f"{lang:<15} {f:>6} {l:>8} {c:>8} {l-c:>8}")
    print("-"*50);print(f"{'Total':<15} {total_f:>6} {total_l:>8} {total_c:>8} {total_l-total_c:>8}")
