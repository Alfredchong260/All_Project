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
import time  # 时间模块, 内置模块
import openpyxl

# 1.找数据对应的地址
url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 2.请求数据
response = requests.get(url=url, headers=headers)
html_data = response.text
# 对比数据(确认数据已经请求下来了)
# print(html_data)


work_book = openpyxl.Workbook()
sheet = work_book.create_sheet('表1')

# 3.解析数据
selector = parsel.Selector(html_data)

lis = selector.xpath('//*[@class="grid_view"]/li')  # 所有的li标签

for li in lis:
    name = li.xpath('.//*[@class="info"]//*[@class="hd"]//a//span[1]/text()').get()
    info = li.xpath('.//*[@class="bd"]//p[1]/text()').get().strip()
    score = li.xpath('.//*[@class="rating_num"]/text()').get().strip()
    follow = li.xpath('.//*[@class="star"]//span[4]/text()').get()
    score = ''.join(score)

    print(name, info, follow, score)
    sheet.append([name, info, follow, score])

work_book.save('豆瓣.xlsx')
