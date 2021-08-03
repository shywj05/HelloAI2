import requests
import json
import speech_recognition as sr

url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = 'adb174ed9071842964dcd029e2ea63d2'

header = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}
r = sr.Recognizer()
while True :
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    with sr.Microphone(sample_rate=16000) as source:
        print()
        print('==== 마이크에 대고 말씀해주세요 ====')
        audio = r.listen(source)
    res = requests.post(url, headers=header, data=audio.get_raw_data())
    try:
        if len(res.text[res.text.index('{"type":"errorCalled"'):res.text.rindex('}')+1])>0 :
            print('음성인식이 안됬습니다')
            continue
    except:
        pass    
    result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
    result = json.loads(result_json_string)
    
    print("인식 결과 : ",result['value'])
    if("종료".__eq__(result['value'])):
        print("====종료되었습니다====")
        break;
    
        

# install 소스

# 1.pip install pipwin
# 2.pipwin install pyaudio
# 3.pip install SpeechRecognition