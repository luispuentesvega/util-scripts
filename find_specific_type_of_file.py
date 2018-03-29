import os
import ntpath

def get_backups():
    arr_files = []
    for r,d,f in os.walk("C://Users/Luis/Documents/BkUriel/Servidores/Servidor Backups/"):
        for files in f:
            if '.dump' in files:
                arr_files.append (os.path.join(r,files))
    return arr_files

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

for backup in get_backups():
    print(path_leaf(backup))
"""This 
ia a comment
ia a comment
"""
"""
dsjdsjkdkjskjdsjkdsk
"""