import requests
from bs4 import BeautifulSoup

url = "https://tw.news.yahoo.com/" 
dow = requests.get(url)
bs = BeautifulSoup(dow.text,"html.parser")

if dow.status_code == 200 :
    print("網頁讀取成功")
    print ("Yahoo 今日新聞焦點")
    print ("-"*40)

    for news in bs.find("ul","H(100%)").find_all("li") :
        print (news.find("a").text)
    
    for news2 in bs.find("ul","H(100%)").find_all("li") :
        print (news2.find("60").text)

else :
    print("網頁讀取失敗")