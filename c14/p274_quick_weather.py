#! python3
# Prints the weather for a location from the command line.

import json
import sys

import requests

if len(sys.argv) < 2:
    print('Usage: quick watther.py location')
    location = 'Beijing'
else:
    location = ' '.join(sys.argv[1:])

# key 需要在官网注册申请，具体看这里: https://openweathermap.org/faq#error401
# api 参考这里
# url1 = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
# url1 = 'https://api.openweathermap.org/data/2.5/weather?q=Beijing&appid=bdacfe9253fb7e249a4956b179c61575'

url1 = 'https://samples.openweathermap.org/data/2.5/forecast?q=%s&appid=bdacfe9253fb7e249a4956b179c61575' % location
print(url1)
# %s 在这里拼接 location
response = requests.get(url1)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['list']

print('Current weather is %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
