from twilio.rest import Client 
import time     
import random  
urlArray = ['https://www.myinstants.com/media/sounds/bkftleetus.mp3','https://www.myinstants.com/media/sounds/vsoss.mp3', 'https://www.myinstants.com/media/sounds/bluelob.mp3', 'https://www.myinstants.com/media/sounds/scamfr.mp3', 'https://www.myinstants.com/media/sounds/underdawater.mp3', 'https://www.myinstants.com/media/sounds/suuuuuu.mp3' ]  
account_sid = 'ACdd5effb2e8049d52b755fd63449a9986' 
auth_token = '20824574373de411974512682d6e3959' 
client = Client(account_sid, auth_token)  
phone_numbers = ['+12076310319', '+13017158592']  
caller_id = '+15155265022'  
for number in phone_numbers:
    print('Calling ' + number)     
    randomUrl = urlArray[random.randint(0, len(urlArray)-1)]        
    call = client.calls.create(
        url= randomUrl,
        to= number,
        from_= caller_id,
        record= True
    )
    time.sleep(1)
