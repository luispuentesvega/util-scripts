import os
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

print(path_leaf('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'))
print(os.getcwd())