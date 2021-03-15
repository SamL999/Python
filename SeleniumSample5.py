from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver") 
driver.implicitly_wait(5)
driver.get("https://hahow.in/courses/")

print (driver.title)
soup = BeautifulSoup(driver.page_source,"lxml")

fp = open("hahow.html", "w", encoding="utf-8")
fp.write(soup.prettify())
print ("寫入檔案 hahow.html....")

fp.close()
driver.quit()

