"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用xpath采集数据
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点
            img_url  # 城市图片url
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

import requests
import parsel

url = 'https://place.qyer.com/china/citylist-0-0-1/'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response = requests.get(url, headers=headers)
selector = parsel.Selector(response.text)
infos = selector.xpath('//ul[@class="plcCitylist"]/li')
for info in infos:
    city_name = info.xpath('./h3/a/text()').get()
    travel_people = info.xpath('./p[@class="beento"]/text()').get()
    travel_hot = info.xpath('./p[@class="pois"]/a/text()').getall()
    img_url = info.xpath('./p[@class="pics"]/a/img/@src').get()
    hots = []
    for hot in travel_hot:
        hots.append(hot.strip())
    print(f"城市名：{city_name}\n去过的人数：{travel_people}\n热门景点：{tuple(hots)}\n城市图片网址：{img_url}\n")
