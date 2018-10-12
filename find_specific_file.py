import os
import ntpath

def main():
	fileName = "Platforms"
	for root,dirs,files in os.walk("C://Users/xxx/"):
		for file in files:
			if fileName in file:
				print("File has been found here ", root)
				exit()
main()
#Response : File has been found here  C://Users/xxx/folder\
