import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/" 
html = requests.get(url)
bs = BeautifulSoup(html.text,"html.parser")

data1 = bs.select(".contents_box02")
data2 = data1[0].find_all("div",{"class":"ball_tx"})

print ("威力彩第一區資料")
print (data2)
print ("="*40)

print ("開出順序 : ",end="")
for i in range(0,6) :
    print (data2[i].text,end=" ")
print ("\n大小順序 : ",end="")
for j in range(6,len(data2)) :
    print (data2[j].text,end=" ")
    
red = data1[0].find("div",{"class":"ball_red"})
print ("\n第二區 : %s " %(red.text))




