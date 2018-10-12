import os, re, os.path

def main():
	mypath = "C://Users/folder/"
	for root, dirs, files in os.walk(mypath):
		for file in files:
			os.remove(os.path.join(root, file))
			
main()