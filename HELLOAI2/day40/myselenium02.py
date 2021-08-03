from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver') 
driver.implicitly_wait(1) 


driver.get('http://127.0.0.1:5000/login.html')
driver.implicitly_wait(1) 

driver.find_element_by_id("user_id").send_keys("S00001")
driver.find_element_by_id("pwd").send_keys("1")
driver.find_element_by_css_selector("input[type=button]").click()
driver.implicitly_wait(1) 

driver.get('http://127.0.0.1:5000/suser')

obj_table = driver.find_element_by_css_selector("body > table > tbody > tr > td:nth-child(1) > table")
obj_trs = obj_table.find_elements_by_tag_name("tr")

for i,tr in enumerate(obj_trs):
    if i > 0 :
        print(tr.find_elements_by_tag_name("td")[1].text,end="\t")
        print(tr.find_elements_by_tag_name("td")[2].text)


html = driver.page_source

# print(html)



# driver.quit()