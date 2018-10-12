import os
import ntpath

def main():
	folderName = "node_modules"
	for root,dirs,files in os.walk("C://folder/"):
		for folder in dirs:
			if folderName in folder:
				print(counter,".The Folder has been found here ", r)
				
main()
#Response : File has been found here  C://Users/xxx/folder\
