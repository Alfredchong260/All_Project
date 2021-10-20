"""
    使用 css 选择器将猫眼 100 十页全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印即可
	温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""

import requests
import parsel
import time


headers = {
    'Host': 'maoyan.com',
    'Referer': 'https://verify.maoyan.com/',
    'user-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def getData(selector):
    infos = selector.css('.movie-item-info')
    marks = selector.css('.movie-item-number.score-num')
    for info, mark in zip(infos, marks):
        name = info.css('p.name>a::text').get()
        star = info.css('.star::text').get().strip()
        release = info.css('.releasetime::text').get()
        integer = mark.css('.integer::text').get()
        fraction = mark.css('.fraction::text').get()
        score = integer + fraction
        proceed = formatter(name, star, release, score)
        yield proceed

def formatter(name, star, release, score):
    information = f'电影名：{name}\n主演：{star}\n上映时间：{release}\n评分：{score}\n'
    return information

def nextPage(page):
    url = f'https://maoyan.com/board/4?offset={page}'
    response = requests.get(url, headers=headers)
    selector1 = parsel.Selector(response.text)

    data = getData(selector=selector1)
    for proceed in data:
        print(proceed)

for page in range(0, 101, 10):
    nextPage(page)
    time.sleep(2)
