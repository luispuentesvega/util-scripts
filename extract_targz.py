import os
import tarfile
import stat
file = 'example.tar.gz'
st = os.stat(file)
oct_perm = oct(st.st_mode)
print(oct_perm)
print(file)
"""
tar = tarfile.open(file)
rta = tar.extractall('D://Luis/Programming/Python/util-scripts-py/20180329')
print(rta)
tar.close()
"""