import re

h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', encoding='utf-8').read()
matches = list(re.finditer(r'[\u4e00-\u9fff]{2,}', h))
seen = set()
out = open(r'D:\Users\Admin\Desktop\航海计算APP\cn_context.txt', 'w', encoding='utf-8')

for m in matches:
    s = m.group()
    if s in seen: continue
    seen.add(s)
    start = max(0, m.start()-80)
    end = min(len(h), m.end()+80)
    ctx = h[start:end].replace('\n', '↵')
    out.write(f'"{s}" at {m.start()}:\n  ...{ctx}...\n\n')

out.close()
print(f'Wrote {len(seen)} Chinese strings to cn_context.txt')
