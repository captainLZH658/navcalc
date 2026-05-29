import re

h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_cur.html', encoding='utf-8').read()
m = re.search(r'<script>(.*?)</script>', h, re.DOTALL)
s = m.group(1)

chunks = re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]+', s)
unique = sorted(set(chunks))
for c in unique:
    print(c)
