html_text = """ <html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>
"""

from bs4 import BeautifulSoup

bs = BeautifulSoup(html_text,"html.parser")

print ("1 : ",bs.title)
print ("\n2 : ",bs.find("a"))
print ("\n3 : ",bs.find("b"))
print ("\n4 : \n",bs.find_all("a",{"class":"union"}))
print ("\n5 : \n",bs.find("a",{"id":"link2"}))
print ("\n6 : \n",bs.find("a",{"href":"http://www.ntu.edu.tw"}))

web = bs.find("a",{"id":"link1"})
print ("\n7 : ",web.get("href"))

data = bs.select(".union")
print ("\n8 : ",data[0].text)
print ("\n9 : ",data[1].text)
print ("\n10 : \n",bs.select("#link3"))



