import urllib.request as ur

url = "https://www.ncu.edu.tw"

res = ur.urlopen(url)

print ("1. 網址 : ",res.geturl(),"\n")
print ("2. 網站讀取狀態 : ",res.status,"\n")
print ("3. 網站表頭資訊 : \n",res.getheaders(),"\n")

content = res.read()

# print ("4. 擷取網站內容(Byte 格式) : ",content)
print ("5. 擷取網站內容(String 格式) : \n",content.decode())