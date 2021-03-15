from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

lotto_list = []

driver = webdriver.Chrome("chromedriver") 
driver.get("https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx")

# 勾選要以年月查詢的選項
driver.find_element_by_id("Lotto649Control_history_radYM").click()
while True :
    select_year = Select(driver.find_element_by_id("Lotto649Control_history_dropYear"))
    year = input("請輸入你要查的樂透年份(從民國103年開始) :")
    print ("請稍後.....")
    select_year.select_by_value(year)
    
    # 找出要查詢的月份
    for i in range(12) :
        selmonth = Select(driver.find_element_by_id("Lotto649Control_history_dropMonth"))
        selmonth.select_by_value(str(i+1))
    
    # 點選查詢
    driver.find_element_by_id("Lotto649Control_history_btnSubmit").click()
    
    # 抓取網頁內容
    html = driver.page_source
    soup = bs(html,"html.parser")
    
    # 計算該網頁中有多少個 table
    tbcount = len(soup.find_all("table", {"class":"td_hm"}))
    
    # 自每一個table抓取樂透號碼，加入 list
    for i in range(tbcount) :
        for j in range(1,7) :
            temp = soup.find("span",{"id" : "Lotto649Control_history_dlQuery_No"+str(j)+"_"+str(i)})
            lotto_list.append(int(temp.text))
    check = input ("還要繼續嗎？ 若要繼續，請輸入 Y(es) \t")
    if check.upper() != "Y" :
        print ("已結束，謝謝！")
        break
    
print (lotto_list)
driver.quit()

