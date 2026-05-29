import re
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', encoding='utf-8').read()
# Check remaining Chinese characters
cn = re.findall(r'[\u4e00-\u9fff]+', h)
if cn:
    print(f"Found {len(cn)} remaining Chinese strings:")
    for s in sorted(set(cn)):
        pass  # print
else:
    print("NO Chinese strings remaining!")
