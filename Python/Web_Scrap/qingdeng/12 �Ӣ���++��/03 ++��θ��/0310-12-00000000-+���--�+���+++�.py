"""
	目标网址: https://cs.lianjia.com/ershoufang/
	
    要求:
		100页数据, 请用多进程方式实现, 需要以下数据:
			room_title = 二手房标题
			room_address = 二手房地址
			room_introduce = 二手房型简介
			room_follow = 关注人数及发布时间
			room_totalPrice = 单价
			room_unitPrice = 总价
			
请在下方编写代码
"""
import concurrent.futures
from tqdm import tqdm
import requests
import csv
import re

url = 'https://cs.lianjia.com/ershoufang/'

headers = {
    'Cookie': 'lianjia_uuid=9b82b6da-5afc-4659-b740-5d56143ee5af; UM_distinctid=17c3aad4d03cd-0f777566bc8f09-142f1c08-2f7600-17c3aad4d0438; _ga=GA1.2.1067420870.1633072018; _smt_uid=6156b395.e596a31; _jzqx=1.1633072018.1633076126.1.jzqsr=google%2Ecom|jzqct=/.-; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217c3aad571d8e3-066bb7d38b6062-142f1c08-3110400-17c3aad571ec4f%22%2C%22%24device_id%22%3A%2217c3aad571d8e3-066bb7d38b6062-142f1c08-3110400-17c3aad571ec4f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; select_city=430100; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1635992955; _jzqc=1; _jzqckmp=1; _qzjc=1; _gid=GA1.2.1422221197.1635992967; _jzqa=1.4508737529290915300.1633072018.1635992956.1635995630.4; CNZZDATA1255849590=792781466-1633064604-%7C1635992627; CNZZDATA1255633284=1217837272-1633062139-%7C1635988324; CNZZDATA1255604082=1781163986-1633062139-%7C1635989400; CNZZDATA1254525948=1279612141-1633071941-%7C1635998275; _qzja=1.1903144296.1633072185851.1635992957485.1635995631277.1635998582821.1635998625837.0.0.0.16.4; _qzjto=6.2.0; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1635998626; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZTQ5NDhlNzhkZmM2NDVhYjBiOTM5NTZjMTQ2NTdiMjlkNGYwNzNlMjYyODI2ZDU2YWUxZDFhOWU1N2VjZDJjMDU3MDVlNzM4MTY3ZGU1OTBjNDEyMmI1ZDhkMDY1NzY3YmIwYWRjZGNiZWYwZDI1NGM3ZWZhOGMyNzkxZGM1NmQyYWY4ZjMzZjFkYjE5YzdhMmY1M2M2YjhkYWUwMDgxNmU3NDIwZmE5MTJhMWJiYjIyODhhYmZkMzRhYWI0NzFlYTQ0NGFkMzAyYTE2ZGExM2RlZmU1MjI2YmVmODc1MTA4ZGY2NDRkZmI2OTRhYTc2ZmExY2FjOGJkN2U2ZTFiZjM5ODU0NTZiMDc3MDBiNzIzOWFhNjI3MmE4MjAwZDNiN2Q2OWNjOWI5M2MyYmI3NTQwMTVjZjAzNmFmZTEzYWQzZGRhNDc3Y2FhZTBiM2IyMWU0OTIyY2ZiMDI1MTZhZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJmYWRhN2E5Y1wifSIsInIiOiJodHRwczovL2NzLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
    'Host': 'cs.lianjia.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}


def sendRequests(url):
    '''此函数为请求指定网址'''
    response = requests.get(url, headers=headers)

    return response

def parseData(response):
    '''此函数为解析网页数据，返回值为压缩的元祖'''
    room_title = re.findall('<a class="title".*?data-el="ershoufang">(.*?)</a>', response.text, re.S)
    addressInfo = re.findall('<a.*?data-el="region">(.*?)</a>(.*?)<a href=".*?" target="_blank">(.*?)</a>', response.text, re.S)
    room_introduce = re.findall('<div class="houseInfo"><span class="\w+"></span>(.*?)</div>', response.text, re.S)
    room_follow = re.findall('<div class="followInfo"><span class="starIcon"></span>(.*?)</div>', response.text, re.S)
    room_unitPrice = re.findall('<div class="unitPrice".*?<span>(.*?)</span></div>', response.text, re.S)
    total = re.findall('<div class="totalPrice totalPrice2">.*?<span>(.*?)</span><i>.*?</i></div>', response.text, re.S)
    room_totalPrice = []
    for i in total:
        room_totalPrice.append(i + '万元')

    room_address = []
    for info in addressInfo:
        room_address.append(info[0].strip() + info[1].strip() + info[2].strip())

    return zip(room_title, room_address, room_introduce, room_follow, room_unitPrice, room_totalPrice)

def writeData(dataList):
    '''此函数用于写入数据'''
    with open('二手屋.csv', 'a', encoding='utf-8') as w:
        csv_writer = csv.writer(w)
        csv_writer.writerow(dataList)

def main(url):
    response = sendRequests(url)
    data = parseData(response)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as exe:
        for i in tqdm(data):
            exe.submit(writeData, i)

'''这段代码为初始化csv文件'''
with open('二手屋.csv', 'w', encoding='utf-8') as w:
    csv_writer = csv.writer(w)
    csv_writer.writerow(['room_title', 'room_address', 'room_introduce', 'room_follow', 'room_unitPrice', 'room_title'])

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as exe:
        for page in range(1, 101):
            url = f'https://cs.lianjia.com/ershoufang/pg{page}/'
            exe.submit(main, url)
