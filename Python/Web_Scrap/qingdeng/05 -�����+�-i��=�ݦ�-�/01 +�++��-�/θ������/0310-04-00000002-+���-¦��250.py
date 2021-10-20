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
import time   # 时间模块, 内置模块




# 1.找数据对应的地址
url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 2.请求数据
response = requests.get(url=url, headers=headers)
html_data = response.text
# 对比数据(确认数据已经请求下来了)
print(html_data)


# 3.解析数据
selector = parsel.Selector(html_data)

lis = selector.css('.grid_view li')  # 所有的li标签

for li in lis:
    name = li.css('.info .hd a span:nth-child(1)::text').get()
    info = li.css('.bd p:nth-child(1)::text').getall()
    score = li.css('.rating_num::text').get().strip()
    follow = li.css('.star span:nth-child(4)::text').get()
    # score = ''.join(score)

    print(name, info, score, follow)