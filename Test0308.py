from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome("chromedriver") 
driver.implicitly_wait(5)
driver.get("https://hahow.in/courses/")

html = driver.page_source
soup = bs(html,"html.parser")  
    
htmlcot = soup.find_all("div", {"class" : "sc-10r5mg2-0 fVNHJD hh-course-brief relative block"})    

for i in htmlcot :               
   if i.find("h4",{"class":"title marg-t-20 marg-b-10"})!=None and i.find("span",{"class":"text-primary"})!=None :
        tittle = i.find("h4",{"class":"title marg-t-20 marg-b-10"})
        print ("課程:", tittle.text)
        price = i.find("span",{"class":"text-primary"})
        print ("預購價:", price.text)
        if i.find("div",{"class":"text-center pad-b-10 incubating"})!=None:
            percentage = i.find("div",{"class":"text-center pad-b-10 incubating"})
            print (percentage.text)

driver.quit()

