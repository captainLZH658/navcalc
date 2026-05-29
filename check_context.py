import re, sys
sys.stdout.reconfigure(encoding='utf-8')

h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', encoding='utf-8').read()
cn_found = list(re.finditer(r'[\u4e00-\u9fff]{2,}', h))
unique = sorted(set(m.group() for m in cn_found))

out = open(r'D:\Users\Admin\Desktop\航海计算APP\context.txt', 'w', encoding='utf-8')
for s in unique:
    idx = h.index(s)
    start = max(0, idx-50)
    end = min(len(h), idx+len(s)+50)
    context = h[start:end].replace('\n', ' ')
    out.write(f'"{s}" => ...{context}...\n\n')
out.close()
print(f'Wrote {len(unique)} strings to context.txt')
