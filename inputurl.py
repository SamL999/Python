import requests as req

url = input("請輸入你要搜尋的網址：")

htmlbody = req.get(url)
htmlbody.encoding = "utf-8"

htmllist = htmlbody.text.splitlines()

n=0

keyword = input("請輸入你要搜尋的字串： ")

for row in htmllist :
    if keyword in row :
        n = n+1
        
print ("\n%s 字串在該網頁中找到 %s 筆 " %(keyword,n))
