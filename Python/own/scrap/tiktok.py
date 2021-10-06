import requests
import random
import re


headers = {
    'Referer': 'https://www.douyin.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']

proxy = {'HTTP': random.choice(proxies)}

url = 'https://www.douyin.com/video/6845907938683505934'

response = requests.get(url, headers=headers, proxies=proxy)
title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text)[0]
id = re.findall('src(.*?)vr3D%2', response.text)
print(response.text)
print(title)
print(id)
