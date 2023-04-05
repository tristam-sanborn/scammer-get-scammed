from twilio.rest import Client
import time
import random

urlArray = ['https://www.myinstants.com/media/sounds/sr-pelo-scream_94hluaY.mp3', 'https://www.myinstants.com/media/sounds/bkftleetus.mp3', 'https://www.myinstants.com/media/sounds/vsoss.mp3', 'https://www.myinstants.com/media/sounds/bluelob.mp3', 'https://www.myinstants.com/media/sounds/scamfr.mp3', 'https://www.myinstants.com/media/sounds/underdawater.mp3', 'https://www.myinstants.com/media/sounds/suuuuuu.mp3' ]

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

phone_numbers = ['+15086412436', '+13512775032']

caller_id = '+15155265022'

for number in phonenumbers:
    print('Calling ' + number)
    randomUrl = urlArray[random.randint(0, len(urlArray)-1)]
    call = client.calls.create(
        url= randomUrl,
        to=number,
        from=caller_id,
        record = True
    )
    time.sleep(1)
