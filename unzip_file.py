import zipfile
import os

with zipfile.ZipFile("bk.zip","r") as zip_ref:
    extracted = zip_ref.namelist()
    zip_ref.extractall(os.getcwd())
    zip_ref.close()
    extracted_file = os.path.join(os.getcwd(), extracted[0])
print("Extracted file "+extracted_file)
