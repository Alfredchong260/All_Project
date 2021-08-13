# 知足的喷瓜
'''
    全局思路：
        爬取数据；书名，类型，简介，多少人读过，多少字，周点击，月点击，更新量, 推荐量
        将书名，类型，简介，多少人读过，多少字，写入txt文件
        将点击量，更新量以及推荐量写入csv文件

    问题：
        1. csv文档:
            csv文档需要标题，当写如标题的操作在写入数据的函数当中时，会发生标题一直重复写入
        2. 榜单分为全部，男生，女生，我爬取了所有榜单，发现某些数据发生重叠
    解决方法：
        1. csv文档：
            把写标题的操作带入另一个新的函数并确保它只运行一次
        2. 把书名记录在列表当中，并用if条件来确定书名没有重复，如重复便跳过，否则，则对数据进行爬取并写入

    结果：
        txt文件有1200行
        csv文档有200行数据(不包括标题)
'''

import requests
import csv
from lxml import etree

url = "https://www.17k.com/top/refactor/top100/10_bookshelf/10_bookshelf_top_100_pc.html"
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

li = []

# 得到需要的数据，书名，类型，简介，多少人读过，多少字
def getInfo(html, title):
    type = html.xpath('//dl[@class="Tab"]/dd/div[2]//tr/td[2]/a/text()')[0]
    intro = html.xpath('//p[@class="intro"]/a/text()')
    read = html.xpath('//div[@class="BookData"]/p[1]/em/text()')[0]
    write = html.xpath('//div[@class="BookData"]/p[2]/em/text()')[0]
    intro = "".join([i.replace("\n", "") for i in intro])
    writeInTXTfile(title=title, intro=intro, type=type, read=read, write=write)

# 获取点击量，更新量以及推荐量的数据
def getData(html):
    week = html.xpath('//td[@id="weekclickCount"]/text()')[0]
    month = html.xpath('//td[@id="monthclickCount"]/text()')[0]
    week_up = html.xpath('//td[@id="hb_week"]/text()')[0]
    month_up = html.xpath('//td[@id="hb_month"]/text()')[0]
    week_sug = html.xpath('//td[@id="flower_week"]/text()')[0]
    month_sug = html.xpath('//td[@id="flower_week"]/text()')[0]
    li = [week, month, week_up, month_up, week_sug, month_sug]
    writeInCSVfile(list=li)

# 将数据写入txt文件当中
def writeInTXTfile(title, intro, type, read, write):
    with open('书籍简介.txt', 'a+') as f:
        f.write(format(title=title, intro=intro, type=type, read=read, write=write))

# 将书籍写入csv文档当中
def writeInCSVfile(list):
    with open('书籍数据.csv', 'a+', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(list)

# 初始化csv文档，写入数据标题
def initialCSV():
    with open('书籍数据.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['本周点击量', '本月点击量', '本周更新量', '本月更新量', '周推荐票', '月推荐票'])

# 设置好要使用的格式
def format(title, intro, type, read, write):
    format =  '''书名    ：{}\n作品类型：{}\n阅读人数：{}\n已写字数：{}\n书籍简介：{}\n\n'''.format(title, type, read, write, intro)
    return format

# 得到内层的URL
def main():
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content.decode('utf-8'))

    results = html.xpath('//div[@class="content TABBOX"]/div[2]/div/table/tr')
    initialCSV()
    for result in results:
        hrefs = result.xpath('./td[3]/a/@href')
        for href in hrefs:
            hr = 'https://www' + href.split('www')[1]
            print(hr)
            response = requests.get(hr, headers=headers)
            html = etree.HTML(response.content.decode('utf-8'))
            title = html.xpath('//div[@class="Info Sign"]/h1/a/text()')[0]

            # 用条件语句来确保没有爬取重复的数据
            if title not in li:
                li.append(title)
                getInfo(html, title)
                getData(html=html)
            else:
                pass

# 调用主函数
main()
