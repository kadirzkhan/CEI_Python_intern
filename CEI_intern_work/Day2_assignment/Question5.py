''' Write a Python program using the requests module to send a GET request to a Given Below Url API endpoint and print the 
a) latitude 
b) longitude 
c) timestamp 
(Url: http://api.open-notify.org/iss-now.json) 
'''

URL = 'http://api.open-notify.org/iss-now.json'

import requests

response = requests.get(URL)
print(response.raise_for_status)

if response.status_code == 200:
    info = response.json()
else:
    raise FileNotFoundError

print('latitude', info['iss_position']['latitude'])
print('longitude', info['iss_position']['longitude'])
print('timestamp', info['timestamp'])