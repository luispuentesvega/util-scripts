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
    #print(path_leaf(backup))
    file = os.path.splitext(path_leaf(backup))
    arr_name = file[0].split('_')
    db_name = arr_name[len(arr_name)-1]
    print("DB Name: "+db_name)
    #print(os.path.splitext(file[0]))
#Output:
#20160615_0803_bd - copia.dump
#20160615_0803_bd.dump
#Getting only the name of the database
