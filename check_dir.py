import os
path = 'D:\\Users\\Admin\\Desktop\\航海计算APP'
for f in os.listdir(path):
    print(f, os.path.getsize(os.path.join(path, f)) if os.path.isfile(os.path.join(path, f)) else '<dir>')