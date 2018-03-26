import os
import datetime

path = os.getcwd()+"\\"+datetime.datetime.now().strftime ("%Y%m%d")
print(os.makedirs(path, exist_ok=True))
