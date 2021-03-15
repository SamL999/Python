import requests,os,urllib
from bs4 import BeautifulSoup

url = "https://www.edu.tw/" 
html = requests.get(url)
html.encoding = "utf-8"
bs = BeautifulSoup(html.text,"html.parser")
pics_dir = "pics"

if not os.path.exists(pics_dir) :
    os.mkdir(pics_dir)

all_link = bs.find_all("img")
for link in all_link :
    src = link.get("src")
    attrs = [src]
    for attr in attrs :
        if attr !=None and ("jpg" in attr or "png" in attr) :
            full_path = attr
            full_n = full_path.split("/")[-1]
            print ("="*30)
            print ("圖檔完整路徑 : ",full_path)
            try :
                image = urllib.request.urlopen(full_path)
                f = open(os.path.join(pics_dir,full_n),"wb")
                f.write(image.read())
                print ("下載成功 : %s" %(full_n))
                f.close()
            except :
                print ("無法下載 : %s" %(full_n))
                
