"""
    目标网址: http://www.zfcg.sh.gov.cn
    作业要求:
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                url    公告详情页地址
                districtName 公告区域
            3. 采集完后打印输出即可
请在下方完成代码:
"""

import requests
import random

url = 'http://www.zfcg.sh.gov.cn/front/search/category'

headers = {
    'Host': 'www.zfcg.sh.gov.cn',
    'Origin': 'http://www.zfcg.sh.gov.cn',
    'Referer':'http://www.zfcg.sh.gov.cn/ZcyAnnouncement/ZcyAnnouncement2/index.html?utm=sites_group_front.2ef5001f.0.0.8485a9002d6d11ec904cadb97c509d18',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
    ]


data = {
    "utm":"sites_group_front.2ef5001f.0.0.8485a9002d6d11ec904cadb97c509d18",
    "categoryCode":"ZcyAnnouncement2",
    "pageSize":50,
    "pageNo":1
}

response = requests.post(url, headers=headers, json=data)
page_num = response.json()['hits']['total']
count = 0
while page_num:
    second_data = data
    headers['User-Agent'] = random.choice(user_agent_list)
    response1 = requests.post(url, headers=headers, json=second_data)
    json_data = response1.json()['hits']['hits']
    for info in json_data:
        print(info['_source']['title'])
        print(info['_source']['url'])
        print(info['_source']['districtName'])
        print()
        count += 1
        page_num -= 1
    second_data['pageNo'] += 1

print(count)
