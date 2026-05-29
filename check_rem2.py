import re, sys
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', encoding='utf-8').read()
cn = re.findall(r'[\u4e00-\u9fff]+', h)
if cn:
    sys.stdout.reconfigure(encoding='utf-8')
    unique = sorted(set(cn))
    print(f"Found {len(unique)} unique Chinese strings:")
    for s in unique:
        print(s)
else:
    print("NO Chinese strings remaining!")
