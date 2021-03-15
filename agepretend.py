import time
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

r = requests.get(url, cookies={"over18":"1"})

if r.status_code == requests.codes.ok :
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text,"lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs :
        if tag.find("a") :
            tag_a = tag.find("a")
            print (tag_a["href"])
            print (tag_a.text)
            print (tag.find("div", class_="author").string)
else :
    print ("HTTP請求錯誤 :"+ url)

