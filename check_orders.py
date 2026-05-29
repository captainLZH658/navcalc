import re
h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', encoding='utf-8').read()
idx = h.find('var ORDERS')
if idx >= 0:
    chunk = h[idx:idx+500]
    print('ORDERS found at', idx)
    print(chunk[:300])
else:
    print('ORDERS not found at any case')
    for case in ['ORDERS', 'orders', 'ORDERS']:
        i = h.find(case)
        if i >= 0:
            print(f'Found {case} at {i}: ...{h[i:i+50]}...')
