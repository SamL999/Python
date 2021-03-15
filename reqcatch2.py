import requests as req

url = "https://data.gov.tw/"

res = req.get(url)

if res.status_code == req.codes.ok :
    print ("成功取得網頁內容")
    print (res.text)
    print ("網頁內容大小 : ",len(res.text))
else :
    print ("無法取得網頁內容")