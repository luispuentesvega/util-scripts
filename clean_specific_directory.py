import os, re, os.path

def main():
	mypath = "C://Users/ruok/Downloads/"
	for root, dirs, files in os.walk(mypath):
		for file in files:
			os.remove(os.path.join(root, file))
			
main()
#Response : File has been found here  C://Users/xxx/folder\
