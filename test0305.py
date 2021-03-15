from selenium import webdriver
from bs4 import BeautifulSoup as bs


driver = webdriver.Chrome("chromedriver") 
driver.implicitly_wait(6)
driver.get("https://www.taiwanlottery.com.tw/lotto/SuperLotto638/history.aspx")

nolist =["105000010", "107000010", "109000010"]

driver.find_element_by_id("SuperLotto638Control_history1_radNO").click()

for i in nolist :
    lotto_list = []
    driver.find_element_by_id("SuperLotto638Control_history1_txtNO").clear()
    driver.find_element_by_id("SuperLotto638Control_history1_txtNO").send_keys(i)
    driver.find_element_by_id("SuperLotto638Control_history1_btnSubmit").click()   
       
    # 抓取網頁內容
    html = driver.page_source
    soup = bs(html,"html.parser")
   
    print('期別：'+soup.find('span',{'id':'SuperLotto638Control_history1_dlQuery_DrawTerm_0'}).text+'\r')  
    
    for i in range(1,8) :
        temp = soup.find("span",{"id" : "SuperLotto638Control_history1_dlQuery_SNo"+str(i)+"_0"})
        lotto_list.append(int(temp.text))
        
    print ("開獎號碼：",str(lotto_list))


driver.quit()
