import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/" 
html = requests.get(url)
bs = BeautifulSoup(html.text,"html.parser")

data1 = bs.select(".contents_box02")
dataa = bs.select(".contents_box04")
data2 = data1[3].find_all("div",{"class":"ball_tx"})
data3 = dataa[1].find_all("div",{"class":"ball_tx"})

d1 = data1[3].find("span",{"class":"font_black15"})
print ("49樂合彩 開獎日期與開獎期數 : ",d1.text)
print ("49樂合彩 中獎號碼 : ",end="")
for i in range(0,6) :
    print (data2[i].text,end=" ")
print ("\n49樂合彩 大小順序 : ",end="")
for j in range(6,len(data2)) :
    print (data2[j].text,end=" ")
    
print (" ")    

d2 = dataa[1].find("span",{"class":"font_black15"})
print ("\n4星彩 開獎日期與開獎期數 : ",d2.text)   
print ("4星彩 中獎號碼 : ",end="")
for k in range(0,4) :
    print (data3[k].text,end=" ")