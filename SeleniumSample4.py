from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


driver = webdriver.Chrome("chromedriver") 
driver.implicitly_wait(10)
driver.get("http://stats.nba.com/players/traditional/?sort=PTS&dir=-1")

page_remaining = True
pageno = 1

while page_remaining :
    soup = bs(driver.page_source,"lxml")
    table = soup.select_one("body > main > div > div > div.row > div > div > nba-stat-table > div.nba-stat-table > div.nba-stat-table__overlay > table")
    df = pd.read_html(str(table))
    df[0].to_csv("AllPlayerStatus"+str(pageno)+".csv")
    print ("儲存頁面 :", pageno)
    try :
        next_link = driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]")
        next_link.click()
        time.sleep(5)
        if pageno < 11 :
            pageno = pageno+1
        else :
            page_remaining = False
    except : 
        page_remaining = False
        
driver.close()