"""
    使用 css 选择器将豆瓣 250 的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250
    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印即可
	温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""

import requests
import parsel
import time


headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/top250',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def formatter(name, informaiton, score, follow):
    data = f'电影名：{name}\n{informaiton}\n评分：{score}\n评价人数：{follow}\n'
    return data

def getInfo(selector):
    infos = selector.css('.info')
    for info in infos:
        name = info.css('.hd a span:nth-child(1)::text').get()
        details = info.css('.bd p::text').getall()
        informaiton = details[0].strip() + '\n' + details[1].strip()
        score = info.css('.star span:nth-child(2)::text').get()
        follow = info.css('.star span:nth-child(4)::text').get()
        data = formatter(name, informaiton, score, follow)
        yield data


for page in range(0, 250, 25):
    url = f'https://movie.douban.com/top250?start={page}'
    response = requests.get(url, headers=headers)
    selector1 = parsel.Selector(response.text)

    datas = getInfo(selector1)
    for data in datas:
        print(data)
    time.sleep(2)
