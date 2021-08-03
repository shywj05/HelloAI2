from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 페이지 가져오기(이동)
driver.get('http://127.0.0.1:5000/')
# html = driver.page_source
driver.find_element_by_xpath('/html/body/a[7]').click()

login_box = driver.find_element_by_id("user_id")
login_box.send_keys("s00001")

login_box = driver.find_element_by_id("pwd")
login_box.send_keys("1")

driver.find_element_by_xpath('/html/body/form/input[3]').click()
driver.get('http://127.0.0.1:5000/suser')


objs_table = driver.find_element_by_css_selector("body>table>tbody>tr>td:nth-child(1)>table")
obj_trs = objs_table.find_elements_by_tag_name("tr")
for i,tr in enumerate(obj_trs):
    if i > 0:
        print(tr.find_elements_by_tag_name("td")[1].text, end = "\t")
        print(tr.find_elements_by_tag_name("td")[2].text)
    
# for i in range(1,4):
# sourcecode_elem = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]").text
#     i = str(i)
#     sourcecode_elem = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr["+i+"]").text
#     sourcecode_elem += sourcecode_elem
# print(sourcecode_elem)


# 5초후 종료
# time.sleep(5)
# driver.quit()