import requests
import os
from tqdm import tqdm
from pprint import pprint

url = 'https://v.6.cn/minivideo/getMiniVideoList.php?act=recommend&page=1&pagesize=30'

headers = {
    'cookie': 'firVist=1631756162; _LiveGuestUser=1169072725%7C%E8%90%8C%E6%96%B0%E5%AE%9D%E5%AE%9Ddz7038; shrek_uuid=B4163175616365607; shrek_reft=23%7C163176189913824; shrek=B4163175616365607%7C163176189913824%7C23; _tracing=index-ipvafi38%7C%7C51787321-0%7C%7C',
    'referer': 'https://v.6.cn/minivideo/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

filename = './video/'

if not os.path.exists(filename):
    os.mkdir(filename)

response = requests.get(url, headers=headers)
infos = response.json()['content']['list']

for info in tqdm(infos):
    url = info['playurl']
    name = url.split('-')[1].split('.')[0]
    respone = requests.get(url, headers=headers)
    with open(filename + name + '.mp4', 'wb') as w:
        w.write(respone.content)
