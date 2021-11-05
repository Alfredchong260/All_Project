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
import csv
import time
import concurrent.futures
import threading
import parsel
import requests


lock = threading.Lock()


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


def send_requests(url):
    response = requests.get(url=url, headers=headers)
    return response.text  # 返回请求的响应体的文本


def parse_data(data):
    selector = parsel.Selector(data)
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')  # 所有li标签
    data_list = []   # 收集解析出来的每一页的地址
    for li in lis:
        city_name = li.xpath('.//h3/a/text()').get()
        travel_people = li.xpath('.//p[@class="beento"]/text()').get()
        travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()
        travel_hot = [hot.strip() for hot in travel_hot]
        travel_hot = '|'.join(travel_hot)
        img_url = li.xpath('.//p[@class="pics"]/a/img/@src').get()
        print(city_name, travel_people, travel_hot, img_url)
        data_list.append([city_name, travel_people, travel_hot, img_url])
    return data_list


def save_data(data_list):
    with open('穷游网.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        for data in data_list:
            lock.acquire()  # 上锁
            csv_write.writerow(data)
            lock.release()  # 解锁


def run(url):
    html_data = send_requests(url)
    parse_list = parse_data(html_data)  # 二维列表的数据
    save_data(parse_list)


# run('https://place.qyer.com/china/citylist-0-0-1/')

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    # 线程池
    for page in range(1, 171):  # 0123456789
        url = f'https://place.qyer.com/china/citylist-0-0-{page}/'
        executor.submit(run, url)

print('花费时间:', time.time() - start_time)