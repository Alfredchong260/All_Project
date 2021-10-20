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
    'Cookie': 'mta=150844937.1628600961648.1634093787397.1634093805737.80; _lxsdk_cuid=17b302e848dc8-055d4409b77c8f-3d740e5b-2f7600-17b302e848dc8; uuid_n_v=v1; uuid=1CCEB4B0228B11EC839DE156DE886F50526DDD9F7C104A1E9486623F8B0EB284; _lxsdk=1CCEB4B0228B11EC839DE156DE886F50526DDD9F7C104A1E9486623F8B0EB284; _csrf=1bb3d9f12059fccc94f76a212a7c1ef48608e2795462a2ca413dd476c68b53cd; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1633074174,1634002670,1634093483,1634125285; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1634125367; __mta=150844937.1628600961648.1634093805737.1634125366799.81; _lxsdk_s=17c79750866-c84-52b-cac%7C%7C7',
    'Referer': 'https://maoyan.com/',
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
