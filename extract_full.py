"""Extract full package and upload assetlinks + PWA files to GitHub"""
import zipfile, os, json, shutil

home = os.path.expanduser('~')
zip_path = os.path.join(home, 'Downloads', '_____pwa.zip')
extract_dir = r'D:\Users\Admin\Desktop\航海计算APP\extracted_pkg'
app_dir = r'D:\Users\Admin\Desktop\航海计算APP'

# Clean and create extract dir
if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)
os.makedirs(extract_dir)

# Extract full ZIP
z = zipfile.ZipFile(zip_path)
z.extractall(extract_dir)
print("Files in package:")
for root, dirs, files in os.walk(extract_dir):
    for f in files:
        fp = os.path.join(root, f)
        print(f"  {os.path.relpath(fp, extract_dir)} ({os.path.getsize(fp)/1024:.0f} KB)")

# Check for assetlinks.json
assetlinks_src = os.path.join(extract_dir, 'assetlinks.json')
if os.path.exists(assetlinks_src):
    with open(assetlinks_src) as f:
        content = f.read()
    print(f"\nassetlinks.json:\n{content[:300]}")
    
    # Save to app dir
    shutil.copy2(assetlinks_src, os.path.join(app_dir, 'assetlinks.json'))
    print("Saved to app dir")

# Check for PWA files
pwa_dir = os.path.join(extract_dir, 'pwa')
if os.path.exists(pwa_dir):
    for f in os.listdir(pwa_dir):
        fp = os.path.join(pwa_dir, f)
        if os.path.isfile(fp):
            shutil.copy2(fp, os.path.join(app_dir, f))
            print(f"Copied {f} to app dir")

print("\nDone extracting")
