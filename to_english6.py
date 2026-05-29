h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_final.html', encoding='utf-8').read()

# Fix last remaining "需求"
h = h.replace('HSFO 需求', 'HSFO Required')
h = h.replace('LSFO 需求', 'LSFO Required')
h = h.replace('MGO 需求', 'MGO Required')

# Also do a comprehensive check for ANY remaining Chinese characters of 2+ chars
import re
cn = re.findall(r'[\u4e00-\u9fff]{2,}', h)
if cn:
    for s in sorted(set(cn)):
        print(f'STILL REMAINING: "{s}"')
else:
    print('ALL CHINESE TEXT REPLACED ✓')

open(r'D:\Users\Admin\Desktop\航海计算APP\index_final.html', 'w', encoding='utf-8').write(h)
print('Saved')
