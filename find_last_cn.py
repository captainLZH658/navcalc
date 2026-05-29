h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_final.html', encoding='utf-8').read()
for i,c in enumerate(h):
    if 0x4E00 <= ord(c) <= 0x9FFF:
        ctx = h[max(0,i-40):i+41].replace('\n',' ')
        print(f'CJK at {i}: U+{ord(c):04X} ({repr(c)}) ...{ctx}...')
