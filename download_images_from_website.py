import datetime
import wget
import ntpath
import os
import urllib
from bs4 import BeautifulSoup

#0.Utils functions
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#1.Create folder for storagin the images
folder = datetime.datetime.now().strftime ("%Y%m%d")
path = os.getcwd()+"\\"+folder
print(os.makedirs(path, exist_ok=True))

#2.Getting url Images from the web site
def get_images(url):
    arr = []
    page = BeautifulSoup(urllib.request.urlopen(url), "html5lib")
    for img in page.findAll('img'):
        print(img['src'])
        arr.append(img['src'])
    return  arr

#3.Download Images
def download_images(arr_urls):
    for url in arr_urls:
        path = os.getcwd()+'/'+folder+'/'+path_leaf(url)
        response = wget.download(url, path)
        print('Downloading %s : rta: %s .... Storage on %s '%(url,response,path))

#Change here the Website
arr_images = get_images("https://wwww.mywebsite.com.co/")
if len(arr_images)>0:
    download_images(arr_images)
else:
    print('Images not found!')