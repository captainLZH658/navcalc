import urllib.request, re

url = 'https://captainlzh658.github.io/navcalc/'
html = urllib.request.urlopen(url).read().decode('utf-8')

m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if m:
    script = m.group(1)
    print(f'Script length: {len(script)}')
    try:
        compile(script, '<script>', 'exec')
        print('No syntax error')
    except SyntaxError as e:
        print(f'Syntax error at line {e.lineno}, col {e.offset}: {e.msg}')
        lines = script.split('\n')
        for i in range(max(0, e.lineno-3), min(len(lines), e.lineno+2)):
            marker = ' >>' if i+1 == e.lineno else '   '
            print(f'{marker} {i+1}: {lines[i]}')
            if i+1 == e.lineno and e.offset:
                print(f'     {" " * (e.offset - 1)}^')
else:
    print('Script not found')
