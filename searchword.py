import requests as req
import re

url = input("請輸入你要搜尋的網址 : ")

res = req.get(url)

if res.status_code == req.codes.ok :
    pattern = input("請輸入你要搜尋的關鍵字 : ")
    if pattern in res.text :
        print ("搜尋 %s 成功" % pattern)
    else :
        print ("搜尋 %s 失敗" % pattern)
    
    times = re.findall(pattern, res.text)
    if times != None :
        print ("%s 出現 %d 次 ! " % (pattern, len(times)))
    else :
        print ("%s 出現 0 次 ! " % pattern ) 

else :
    print ("無法取得網頁內容")
