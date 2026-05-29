import re
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english2.html', encoding='utf-8').read()

# Fix remaining individual issues
fixes = {
    # "尾风" - fix the Port Quarter label generation
    "Port尾风 (Port Quarter, ": "Port Quarter (",
    "Stbd尾风 (Stbd Quarter, ": "Stbd Quarter (",
    
    # "往返" - direction selector label
    'class="field-label">往返</div>': 'class="field-label">Direction</div>',
    
    # "燃油需求" + "需求" - calc button
    '🧮 Calculate燃油需求': '🧮 Calculate Fuel Required',
    
    # "系泊" - night orders category
    "系泊": "Mooring",
    
    # "装卸" - night orders category  
    "装卸": "Cargo Ops",
    
    # "重载" - fuel direction selector
    '重载 Laden': 'Laden',
    'Ballast Ballast': 'Ballast',
    
    # "Laden大副": fix mixed language
    'Laden大副': 'Chief Officer (Laden)',
    
    # Also check for any "大副", "二副", "三副" etc.
    '大副': 'Chief Officer',
    '二副': '2nd Officer',
    '三副': '3rd Officer',
}

for old, new in fixes.items():
    if old in h:
        h = h.replace(old, new)
        pass
    else:
        pass

# Check remaining Chinese
remaining = re.findall(r'[\u4e00-\u9fff]{2,}', h)
print(f'\nRemaining Chinese: {len(set(remaining))}')
if remaining:
    for s in sorted(set(remaining)):
        pass

open(r'D:\Users\Admin\Desktop\航海计算APP\index_english2.html', 'w', encoding='utf-8').write(h)
print('\nSaved')
