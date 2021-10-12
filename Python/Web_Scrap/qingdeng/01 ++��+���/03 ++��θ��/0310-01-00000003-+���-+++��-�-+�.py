"""
上课爬取图片的案例

	课上讲解是的爬取 香气四溢的薯条 (1/10) 这个系列图片,
	这个系列一共十张, 要求大家一次性将一个系列图片全部爬取下来

	地址： https://www.hexuexiao.cn/a/124525.html

请下下方开始编写代码
"""

from tqdm import tqdm
import requests
import re
import os

filename = './薯条'
if not os.path.exists(filename):
    os.mkdir(filename)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

url = f'https://www.hexuexiao.cn/a/124525.html'
response = requests.get(url, headers=headers)
links = re.findall("<div class='swiper-slide'><a.*?<img src='(.*?)' />", response.text)

for link in tqdm(links):
    link = link.split('.300')[0]
    name = link.split('/')[-1]
    response = requests.get(link, headers=headers)
    with open(f"{filename}/{name}", 'wb') as w:
        w.write(response.content)
