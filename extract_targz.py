import tarfile
tar = tarfile.open("samples.tar.gz")
tar.extractall('D://Luis/Programming/Python/util-scripts-py/20180329')
tar.close()