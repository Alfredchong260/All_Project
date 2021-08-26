import requests
import json

url = 'https://api.iyk0.com/bilibili'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Cookie': 'PHPSESSID=lr82289slr6lm8vro9de1n9f8n; Hm_lvt_dc99367dbe3e7a89053dcc51df3673b4=1629898783; Hm_lpvt_dc99367dbe3e7a89053dcc51df3673b4=1629898847; UM_distinctid=17b7d89c0c62f3-0ee95af9c31d088-376a464a-8e3c7-17b7d89c0c7379; CNZZDATA1280091788=1323214203-1629898784-https%253A%252F%252Fduckduckgo.com%252F%7C1629898784'
}

param = {
    'msg': 'blackpink',
    'b': 1,
    'title': 'blackpink house'
}
response = requests.post(url, headers=headers, params=param)
print(response)
print(response.json())
