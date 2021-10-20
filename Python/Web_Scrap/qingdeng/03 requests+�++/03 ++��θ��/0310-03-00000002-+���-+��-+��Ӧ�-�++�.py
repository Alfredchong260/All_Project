"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""

'''
全局思路：
    1. 先得到总共有多少条数据
    2. 利用while循环来判断写入多少次数据
    3. 整合需要的数据
    4. 格式化数据
    5. 写入txt文档
    6. 每写入一组数据便减少while循环的条件
'''

from tqdm import tqdm
import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

headers = {
    'Host': 'www.kfc.com.cn',
    'Origin': 'http://www.kfc.com.cn',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

params = {
    'op': 'keyword'
}

data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': 1,
    'pageSize': 10
}

def formatter(store, details, situation):

    format = f"店名：{store}\n地址：{details}\n详情：{situation}\n\n"

    return format


def page(data):
    for keyword in keywords:
        second_data = data
        second_data['keyword'] = keyword
        response = requests.post(url, headers=headers, data=second_data, params=params)
        num = response.json()['Table'][0]['rowcount']
        yield [num, keyword, second_data]


def getData(pages, second_data, keyword):
    print(f"正在查询{keyword}")
    while pages:
        response1 = requests.post(url, headers=headers, data=second_data, params=params, allow_redirects=False)
        json_data = response1.json()['Table1']
        for data in tqdm(json_data):
            store = data['storeName']
            details = data['addressDetail']
            situation = data['pro']
            info = formatter(store, details, situation)
            with open(f"{keyword}.txt", 'a') as w:
                w.write(info)
            pages -= 1
        second_data['pageIndex'] += 1
        print(pages)
    second_data['pageIndex'] = 1

def getInfo():
    while True:
        keyword = input('默认自动查询北京，上海，广州\n请输入要查询的城市：')
        if keyword == '':
            break
        keywords.append(keyword)

keywords = ['北京', '上海', '广州']

getInfo()
nums = page(data)
for num in nums:
    getData(pages=num[0], second_data=num[2], keyword=num[1])
