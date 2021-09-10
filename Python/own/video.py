import requests
import re
import os

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'referer': 'https://music.163.com/'
}

url = 'https://music.163.com/discover/toplist?id=3778678'

path = './music'
if not os.path.exists(path):
    os.mkdir('./music')

response = requests.get(url, headers=headers)

html = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)

response.close()

for id, title in html:
    url = f"https://music.163.com/outchain/player?type=2&id={id}"
    response = requests.get(url, headers=headers)
    with open('./music/' + title + '.mp3', mode='wb') as music:
        music.write(response.content)

    print(f'正在下载{title}.mp3文件')
