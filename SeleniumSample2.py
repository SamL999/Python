from selenium import webdriver
import os

driver = webdriver.Chrome("chromedriver") 
driver.implicitly_wait(6)
html = os.path.abspath("SeleniumTest.html")
driver.get(html)

try : 
    # 使用 selenium 定位函數解析
    h3 = driver.find_element_by_tag_name("h3")
    print (h3.text)
    p = driver.find_element_by_tag_name("p")
    print (p.text)
    
    print ("-"*40)
    
    content = driver.find_element_by_class_name("content")
    print (content.text)
    
    print ("-"*40)
    
    # 使用 css選擇器 定位網頁資料
    content = driver.find_element_by_css_selector("h3.content")
    print (content.text)
    p = driver.find_element_by_css_selector("p")
    print (p.text)
    
    print ("-"*40)
    
    # 使用 id屬性 定位網頁資料
    form = driver.find_element_by_id("loginForm")
    print (form.tag_name)
    print (form.get_attribute("id"))
    
    print ("-"*40)
    
    # 使用 超連結 定位網頁資料
    link1 = driver.find_element_by_link_text("Continue")
    print (link1.text)
    link2 = driver.find_element_by_partial_link_text("Cont")
    print (link2.text)
    
    print ("-"*40)
    
    # 使用 name屬性 定位網頁資料
    user = driver.find_element_by_name("username")
    print (user.tag_name)
    print (user.get_attribute("type"))
    eles = driver.find_elements_by_name("continue")
    for e in eles:
        print (e.get_attribute("type"))

except :
    print ("選取元素不存在 !!!")
driver.quit()

