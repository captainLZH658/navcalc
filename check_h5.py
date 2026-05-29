import re

h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_cur.html', encoding='utf-8').read()
m = re.search(r'<script>(.*?)</script>', h, re.DOTALL)
s = m.group(1)

tools = ['rETA', 'rDensity', 'rCargo', 'rFuel', 'rDew', 'rSquat', 'rWind', 'rNight']
for t in tools:
    idx = s.find('function ' + t)
    if idx >= 0:
        end = s.find('\n}\n', idx)
        if end < 0: end = idx + 500
        print(f'=== {t} ({end-idx} chars) ===')
        part = s[idx:min(idx+200, end)]
        print(part)
        print()
    else:
        print(f'{t}: NOT FOUND')
