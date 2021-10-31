

"""
时间戳的概念:
    从格林威治时间 1970年1月1日0时0分0秒   到   目前所消耗的时间数
        秒级时间戳: 10位数字
        毫秒级时间戳: 13位数字
        微秒级时间戳: 16位数字

"""
import csv
import pprint
import time


# def get_time():
#     """获取时间戳"""
#     now_time = str(int(time.time() * 1000))
#     print(now_time)
#
# get_time()

# 时间戳一般在网页中, 记录你当前访问的时间
# 时间戳后台校验不校验, 也要具体情况具体分析

# 1.找数据请求地址
import requests

url = 'https://index.mysteel.com/zs/newprice/getChartMultiCity.ms'

params = {
'catalog': '%E7%BA%BF%E6%9D%90_:_%E7%BA%BF%E6%9D%90',
'city': '%E6%9D%AD%E5%B7%9E',
'spec': '6%E9%AB%98%E7%BA%BFHPB300_:_HPB300_6%E9%AB%98%E7%BA%BF',
'startTime': '2021-07-01',
'endTime': '2021-10-01',
'callback': 'json',
'v': '1635335380112',  # 时间戳有没有过期, 以及什么时候过期, 可以测试得到结果
}

headers = {
    'Cookie': 'Hm_lvt_1c4432afacfa2301369a5625795031b8=1635334024; Hm_lpvt_1c4432afacfa2301369a5625795031b8=1635334024; qimo_seosource_5d36a9e0-919c-11e9-903c-ab24dbab411b=%E7%AB%99%E5%86%85; qimo_seokeywords_5d36a9e0-919c-11e9-903c-ab24dbab411b=; qimo_xstKeywords_5d36a9e0-919c-11e9-903c-ab24dbab411b=; href=https%3A%2F%2Findex.mysteel.com%2Fprice%2FindexPrice.html; accessId=5d36a9e0-919c-11e9-903c-ab24dbab411b; pageViewNum=1',
    'Host': 'index.mysteel.com',
    'Referer': 'https://index.mysteel.com/price/indexPrice.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}

# 2. 发送请求
response = requests.get(url=url, params=params, headers=headers)
json_data = response.json()
# pprint.pprint(json_data)

# 数据解析
city_name = json_data['data'][0]['lineName']
dateValueMap = json_data['data'][0]['dateValueMap']
print(city_name)

with open('钢铁数据.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_write = csv.DictWriter(f, fieldnames=['city', 'date', 'value'])
    csv_write.writeheader()

    for data in dateValueMap:
        data['city'] = city_name
        print(data)
        csv_write.writerow(data)


"""
能不能用session?
可不可以用session?

    维持你请求的状态, 比如登录状态...
"""