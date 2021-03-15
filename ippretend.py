from bs4 import BeautifulSoup
import requests
import random

# 代理伺服器查詢網站  http://cn-proxy.com  http://www.freeproxylists.net/
proxy_ips = ["51.83.193.208:80", "112.169.9.162:80","47.242.78.34:8000",
             "138.199.29.145:3128", "206.189.132.13:8080"]
ip = random.choice(proxy_ips)
print ("Current use IP Address :", ip) 

res = requests.get("http://ip.filefab.com/index.php", proxies={"http":"http://" + ip})
soup = BeautifulSoup(res.text,"html5lib")
print (soup.find("h1", id="ipd").text.strip())