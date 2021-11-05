"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用多线程采集170页所有数据保存为csv, 计算程序运行的时间
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点  比如香港有热门景点[ 香港海洋公园 、 星光大道 、 维多利亚港 、 太平山 、 尖沙咀 、 金紫荆广场 、 香港迪士尼乐园 、 中环 、 弥敦道 、 兰桂坊 、 中银大厦 、 香港杜莎夫人蜡像馆 、 中环至半山自动扶]
            img_url  # 城市图片url
            
请在下方编写代码：
"""
import concurrent.futures
from tqdm import tqdm
import requests
import parsel
import time
import csv


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

def sendRequests(url):
    '''此函数为首次访问页面'''
    response = requests.get(url, headers=headers)
    selector = parsel.Selector(response.text)

    return selector

def parseData(selector):
    '''此函数为解析页面数据并返回'''
    infos = selector.css('.plcCitylist li')
    for info in infos:
        newPlace = []
        cityName = info.css('.title.fontYaHei>a::text').get()
        travel_people = info.css('.beento::text').get()
        travel_hot = info.css('.pois a::text').getall()
        for hot in travel_hot:
            newPlace.append(hot.strip())
        img_url = info.css('.pics img::attr(src)').get()
        yield [cityName, travel_people, newPlace, img_url]

def writeData(dataList):
    '''此函数为写入数据'''
    with open('qiongyou.csv', 'a', encoding='utf-8') as w:
        csv_writer = csv.writer(w)
        csv_writer.writerow(dataList)

def main(url):
    '''主函数'''
    selector = sendRequests(url)
    data_list = parseData(selector)

    for data in tqdm(data_list, desc='写入数据'):
        writeData(data)

# 初始化csv文件，写入标头
with open('qiongyou.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['City Name', 'Travel People', 'Travel Hot', 'Img Url'])

start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as exe:
    for page in range(1, 171):
        url = f'https://place.qyer.com/china/citylist-0-0-{page}/'
        exe.submit(main, url)

print('爬虫用时：', time.time() - start)
