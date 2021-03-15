import time
import requests

url = "http://www.momoshop.com.tw/search/"

fh = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

r = requests.get(url + "searchShop.jsp?keyword=HTC", headers=fh)

if r.status_code == requests.codes.ok :
    r.encoding = "big5"
    print (r.text)
else :
    print ("HTTP請求錯誤 :"+ url)
  

