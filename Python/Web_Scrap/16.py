from functools import wraps
from os import write
import requests
import re
import os

# obj = re.compile(r"url: '(.*?)',", re.S)
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
# url = 'https://www.91kanju.com/vod-play/12931-1-1.html'

# response = requests.get(url, headers=headers)
# m3u8_url = obj.search(response.text).group(1)
# print(m3u8_url)
# response.close()

# response2 = requests.get(m3u8_url, headers=headers)

# with open('huangye.m3u8', mode='wb') as f:
#     f.write(response2.content)

os.mkdir('video')
n = 1
with open('huangye.m3u8', mode='r', encoding='utf-8') as r:
    for lines in r:
        line = lines.strip() # 去掉空白，空行
        if line.startswith('http'):
            response3 = requests.get(url=line, headers=headers)
            f = open(f"./video/{n}.ts", 'wb')
            f.write(response3.content)
            f.close()
            response3.close()
            print('完成一个')
            n += 1

