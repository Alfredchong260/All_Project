"""
将上课的案例-爬取小说完善。爬取《剑来》前面十章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.biquge7.com/book/1031/

请下下方开始编写代码
"""

from tqdm import tqdm
import requests
import re
import os

filename = './剑来/'

if not os.path.exists(filename):
    os.mkdir(filename)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

for page in tqdm(range(1, 11)):
    url = f'https://www.biquge7.com/book/1031/{page}.html'
    response = requests.get(url, headers=headers)
    obj = re.compile('<div id="\w+" class="\w+\s\w+">(.*?)<p class="\w+">', re.S)
    info = re.findall(obj, response.text)
    name = re.findall('<meta name="keywords" content="剑来,(\w+\s\w+)"/>', response.text)
    for i in info:
        data = i.strip().split('<br />')
        information = '\n'.join(data)
        with open(f'{filename}{name[0]}.txt', 'w') as w:
            w.write(information)
print('下载完成')
