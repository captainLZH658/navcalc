import urllib.request, re, sys

url = 'https://captainlzh658.github.io/navcalc/index.html'
html = urllib.request.urlopen(url).read().decode('utf-8')

# Show raw rep of first 100 chars around the ORDERS array
print(f"Total HTML length: {len(html)}")

# Find the script content
m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if not m:
    print("NO SCRIPT TAG FOUND!")
    sys.exit(1)

script = m.group(1)
print(f"Script length: {len(script)}")

# Count all occurrences of text:" followed by various patterns
count_text_quote = len(re.findall(r'text:"', script))
count_text_double_quote = len(re.findall(r'text:""', script))

print(f"Occurrences of text:\": {count_text_quote}")
print(f"Occurrences of text:\"\": {count_text_double_quote}")

# Show all lines with text:" to understand the pattern
lines = script.split('\n')
print("\nLines containing 'text:':")
for i, ln in enumerate(lines):
    idx = ln.find('text:')
    if idx >= 0:
        snippet = ln[idx:idx+60]
        print(f"  L{i+1}: {repr(snippet)}")
