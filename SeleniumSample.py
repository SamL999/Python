from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver") 
driver.implicitly_wait(5)
driver.get("http://example.com")

print (driver.title)
soup = BeautifulSoup(driver.page_source,"lxml")

fp = open("index.html", "w", encoding="utf-8")

# fp.write(soup.prettify())
# print ("寫入檔案 index.html....")
# fp.close()


# 使用 selenium 定位函數解析
h1 = driver.find_element_by_tag_name("h1")
print (h1.text)
p = driver.find_element_by_tag_name("p")
print (p.text)

print ("-"*40)

# 使用 BeautifulSoup 定位函數解析
tag_h1 = soup.find("h1")
print (tag_h1.text)
tag_p = soup.find("p")
print (tag_p.text)


driver.quit()

