import re, sys
sys.stdout = open(r'D:\Users\Admin\Desktop\航海计算APP\fix_report.txt', 'w', encoding='utf-8')

h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english2.html', encoding='utf-8').read()

# Fix remaining individual issues
fixes = {
    # "尾风" - fix the Port Quarter label generation
    "Port尾风 (Port Quarter, ": "Port Quarter (",
    "Port尾风": "Port Quarter",
    "Stbd尾风": "Stbd Quarter",
    "尾风": "Quarter",
    
    # "往返" - direction selector label
    'class="field-label">Direction': 'class="field-label">Voyage Type',  # already fixed
    
    # "燃油需求" + "需求" - calc button
    'Calculate Fuel Required': '',
    '🧮 Calculate Fuel Required': '🧮 Calculate Fuel Required',
    
    # "系泊" - night orders category
    "系泊": "Mooring",
    
    # "装卸" - night orders category  
    "装卸": "Cargo Ops",
    
    # "重载" - fuel direction selector
    'Laden Laden': 'Laden',
    'Ballast Ballast': 'Ballast',
    'Laden': 'Laden',
    
    # Duplicate issues
    '🧮  Calculate Fuel Required': '🧮 Calculate Fuel Required',
}

for old, new in fixes.items():
    n = h.count(old)
    if n > 0:
        h = h.replace(old, new)
        print(f'Fixed {n}x: {repr(old)} -> {repr(new)}')
    else:
        print(f'NOT FOUND: {repr(old)}')

remaining = list(set(re.findall(r'[\u4e00-\u9fff]{2,}', h)))
print(f'\nRemaining Chinese strings: {len(remaining)}')
for s in sorted(remaining):
    idx = h.index(s)
    start = max(0, idx-40)
    end = min(len(h), idx+len(s)+40)
    ctx = h[start:end].replace('\n', ' ')
    print(f'  "{s}" ...{ctx}...')

open(r'D:\Users\Admin\Desktop\航海计算APP\index_english3.html', 'w', encoding='utf-8').write(h)
print('\nSaved index_english3.html')
