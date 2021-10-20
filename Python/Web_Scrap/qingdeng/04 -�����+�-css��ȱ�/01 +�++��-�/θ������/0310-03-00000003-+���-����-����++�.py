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


url = 'http://www.zfcg.sh.gov.cn/front/search/category'

data = {
    'categoryCode': "ZcyAnnouncement3012",
    'pageNo': '1',
    'pageSize': '15',
    'utm': "sites_group_front.2ef5001f.0.0.3fd619e02db111ec91fad3aab94c109b"
}

headers = {
    'Cookie': '_zcy_log_client_uuid=46888ff0-8f07-11eb-8dfa-4355d4217111',
    'Host': 'www.zfcg.sh.gov.cn',
    'Origin': 'http://www.zfcg.sh.gov.cn',
    'Referer': 'http://www.zfcg.sh.gov.cn/ZcyAnnouncement/index.html?utm=sites_group_front.2ef5001f.0.0.3fd619e02db111ec91fad3aab94c109b',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

response = requests.post(url=url, json=data, headers=headers)
json_data = response.json()
print(json_data)

data_list = json_data['hits']['hits']

for lis in data_list:
    title = lis['_source']['title']
    url = lis['_source']['url']
    districtName = lis['_source']['districtName']
    print(title, url, districtName, sep=' | ')

# Ctrl + X 剪切
