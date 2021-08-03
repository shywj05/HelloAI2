from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
import speech_recognition as sr

class MyCrawler():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('http://127.0.0.1:5000/login.html')

        login_box = self.driver.find_element_by_id("user_id")
        login_box.send_keys("s00001")
        
        login_box = self.driver.find_element_by_id("pwd")
        login_box.send_keys("1")
        self.driver.find_element_by_xpath('/html/body/form/input[3]').click()
        self.driver.get('http://127.0.0.1:5000/sdetail?survey_id=1')

    def crawl(self):
        obj_table = self.driver.find_element_by_css_selector("body > table > tbody > tr > td:nth-child(1) > table")
        obj_trs = obj_table.find_elements_by_tag_name("tr")
        for i,tr in enumerate(obj_trs):
            if i > 0 :
                print(tr.find_elements_by_tag_name("td")[0].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[1].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[2].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[3].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[4].text,end="\t")
                print(tr.find_elements_by_tag_name("td")[5].text)
        

#         
#         self.myspeak()
# 
# 
#             
#     def myspeak(self):
#         url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
#         
#         rest_api_key = 'adb174ed9071842964dcd029e2ea63d2'
#         
#         header = {
#             "Content-Type": "application/octet-stream",
#             "X-DSS-Service": "DICTATION",
#             "Authorization": "KakaoAK " + rest_api_key,
#         }
#         r = sr.Recognizer()
#         while True :
#             
#             with sr.Microphone(sample_rate=16000) as source:
#                 print()
#                 print('==== 마이크에 대고 말씀해주세요 ====')
#                 audio = r.listen(source)
#             res = requests.post(url, headers=header, data=audio.get_raw_data())
#             try:
#                 if len(res.text[res.text.index('{"type":"errorCalled"'):res.text.rindex('}')+1])>0 :
#                     print('음성인식이 안됬습니다')
#                     continue
#             except:
#                 pass    
#             result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
#             result = json.loads(result_json_string)
#             
#             print("인식 결과 : ",result['가져'])
#             if("종료".__eq__(result['value'])):
#                 print("====종료되었습니다====")
#                 break;
            


if __name__ == "__main__":
    mc = MyCrawler()
    mc.crawl()
    
    
    
    
    
    
    
    
    
    
    
    
