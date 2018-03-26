import os

#Printing file from a route
dir = os.getcwd()
for entry in os.scandir(dir):
    if entry.is_file():
        print(entry.name)
