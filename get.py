import requests
import time


for i in range(1):
    response =requests.get('https://www.maduraonline.com/?find=cat')
    # type(response) - it is a class >> <class 'request.model.Response'>
    print(response.text.encode('utf-8'))
    time.sleep(1)



