import os
total_size = 0
start_path = 'This PC\Luis Puentes (Galaxy A5)\Card'  # To get size of current directory
for path, dirs, files in os.walk(start_path):
    for f in files:
        fp = os.path.join(path, f)
        total_size += os.path.getsize(fp)
print("Directory size: " + str(total_size))