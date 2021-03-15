import time
import requests

url = "http://www.majortests.com/word-lists/word-list-0{0}.html"

for i in range(1,10) :
    url = url.format(i)
    r = requests.get(url)
    print (r.status_code)
    print ("等待5秒再存取網頁 !")
    time.sleep(5)

