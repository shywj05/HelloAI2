import os
from twilio.rest import Client

class MySms:
    def mysendSms(self,mobile, content):
        account_sid = 'ACb5f9dacf9e30077d8b91db20742967d0'
        auth_token = 'd7410be1db377c9a1fd0920b17641961'
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            to="+82"+mobile, 
            from_="+13172254351",
            body=content)
    
if __name__ == '__main__':
    MySms().mysendSms("01058261270", "http://127.0.0.1:5000")
    
# 010-9336-7026 김현주
# 010-5826-1270 길정우