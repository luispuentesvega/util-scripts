import tarfile
tar = tarfile.open("samples.tar.gz")
tar.extractall()
tar.close()