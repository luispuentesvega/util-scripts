import os
for r,d,f in os.walk("C://"):
    for files in f:
        if '.tar.gz' in files:
            print(os.path.join(r,files))