import re
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_final.html', encoding='utf-8').read()

# Find all '需求' occurrences
for m in re.finditer('需求', h):
    ctx = h[max(0,m.start()-30):m.end()+30].replace('\n',' ')
    print(f'at {m.start()}: ...{ctx}...')

# Count remaining Chinese
cn = re.findall(r'[\u4e00-\u9fff]{2,}', h)
print(f'\nUnique Chinese strings: {len(set(cn))}')
for s in sorted(set(cn)):
    print(f'  "{s}"')
