"""
	目标地址：https://maoyan.com/board/4?offset=0
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""

from tqdm import tqdm
import requests
import time
import re

'''1'''
headers = {
    'Host': 'maoyan.com',
    'Referer': 'https://verify.maoyan.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

for page in range(0, 101, 10):
    url = f'https://maoyan.com/board/4?offset={page}'
    time.sleep(1)
    response = requests.get(url, headers=headers)
    titles = re.findall('<a href=".*?" title="\w+" data-act="boarditem-click" data-val="{movieId:\d+}">(\w+)</a>', response.text, re.S)
    actors = re.findall('<p class="star">\s+(.*?)\s+</p>', response.text, re.S)
    dates = re.findall('<p class="releasetime">(.*?)</p>', response.text, re.S)
    ratings = re.findall('<i class="integer">(\d{1,2}.)</i><i class="fraction">(\d)</i>', response.text, re.S)

    with open('./电影信息.txt', 'a', encoding='utf-8') as w:
        for title, actor, date, rating in tqdm(zip(titles, actors, dates, ratings)):
            first = f"电影名字:{title}"
            second = actor
            third = date
            forth = f"评分:{rating[0]}{rating[1]}"
            w.write(f"{first}\n{second}\n{third}\n{forth}\n\n")

'''2'''
# Cookies
# Host
# Referer
# User-Agent
