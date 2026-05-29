import re
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english2.html', encoding='utf-8').read()
remaining = list(set(re.findall(r'[\u4e00-\u9fff]{2,}', h)))
out = open(r'D:\Users\Admin\Desktop\航海计算APP\rem_context.txt', 'w', encoding='utf-8')
for s in sorted(remaining):
    idx = h.index(s)
    start = max(0, idx-60)
    end = min(len(h), idx+len(s)+60)
    ctx = h[start:end].replace('\n', ' ')
    out.write(f'"{s}": ...{ctx}...\n\n')
out.close()
print(f'Found {len(remaining)} remaining strings')
