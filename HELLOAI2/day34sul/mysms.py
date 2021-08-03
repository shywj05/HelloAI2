import os
from twilio.rest import Client

class MySms:
    def mysendSms(self, mobile, content):
        account_sid = 'ACfb7be0944c6ac943c3d884fa14f6cb08'
        auth_token = 'be2b5a982d1be29b79f4841201c50856'
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            to="+82" + mobile, 
            from_="+14076413470",
            body=content)

if __name__ == '__main__':
    MySms().mysendSms("01049456804", "http://127.0.0.1:5000")
        
