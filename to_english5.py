import re
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english3.html', encoding='utf-8').read()

# Fix last 4 Chinese strings
# 1. "燃油需求" + "需求" in calc button
h = h.replace('🧮 Calculate燃油需求', '🧮 Calculate Fuel Required')

# 2. "往返" as field label 
h = h.replace('class="field-label">往返', 'class="field-label">Direction')

# 3. "重载" in select option  
h = h.replace('重载 Laden', 'Laden')

# Fix the "Ballast Ballast" issue  
h = h.replace('Laden</option><option value="ballast">Ballast</option>', 'Laden</option><option value="ballast">Ballast</option>')

# Check remaining
remaining = list(set(re.findall(r'[\u4e00-\u9fff]{2,}', h)))
print(f'Remaining: {len(remaining)}')
for s in sorted(remaining):
    idx = h.index(s)
    ctx = h[max(0,idx-30):idx+len(s)+30].replace('\n',' ')
    print(f'  "{s}" ...{ctx}...')

open(r'D:\Users\Admin\Desktop\航海计算APP\index_final.html', 'w', encoding='utf-8').write(h)
print('Saved index_final.html')
