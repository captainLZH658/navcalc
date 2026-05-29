import urllib.request, re

url = 'https://captainlzh658.github.io/navcalc/'
html = urllib.request.urlopen(url).read().decode('utf-8')

m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if m:
    script = m.group(1)
    lines = script.split('\n')
    # Show lines around the error (line 98)
    for i in range(94, min(len(lines), 110)):
        print(f'{i+1:3d}: {repr(lines[i][:100])}')
