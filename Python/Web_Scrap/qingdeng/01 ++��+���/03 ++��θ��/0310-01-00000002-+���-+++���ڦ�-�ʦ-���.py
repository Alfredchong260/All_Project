"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
"""请下下方开始编写代码"""

import concurrent.futures
from tqdm import tqdm
import requests
import re
import os

filename = './sticker'
if not os.path.exists(filename):
    os.mkdir(filename)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

def main(page):
    url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    response = requests.get(url, headers=headers)
    obj = re.compile('<img class="ui image lazy" data-original="(.*?)" src=".*?" title=".*?" alt=".*?" style=".*?"/>', re.S)
    data = re.findall(obj, response.text)
    for url in tqdm(data):
        response = requests.get(url, headers=headers)
        name = url.split('/')[-1]
        with open(f"{filename}/{name}", 'wb') as w:
            w.write(response.content)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
        for page in range(1, 11):
            exe.submit(main, page)
