"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""
import requests

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


def get_page(city_name):
    """分析每个城市的页数"""
    data = {
        'cname': '',
        'pid': '',
        'keyword': city_name,
        'pageIndex': '1',
        'pageSize': '10',
    }
    response = requests.post(url=base_url, data=data, headers=headers)
    json_data = response.json()
    rowcount = json_data['Table'][0]['rowcount']
    # print(rowcount)

    if rowcount % 10 > 0:
        page = rowcount // 10 + 1
    else:
        page = rowcount // 10
    return page


def send_requests(city_name):
    page = get_page(city_name)

    for p in range(1, page + 1):
        print(f'正在抓取 -{city_name}- 数据, 目前是第 ={p}= 页')
        data = {
            'cname': '',
            'pid': '',
            'keyword': city_name,
            'pageIndex': str(p),
            'pageSize': '10',
        }

        # 2. 请求数据
        # data 关键字传递post请求提交的请求参数
        response = requests.post(url=base_url, headers=headers, data=data)
        json_data = response.json()
        # print(json_data)

        # 解析数据
        data_list = json_data['Table1']
        for ls in data_list:
            storeName = ls['storeName']
            addressDetail = ls['addressDetail']
            pro = ls['pro']
            print(storeName, addressDetail, pro)


city_list = ['北京', '广州', '上海']
for city in city_list:
    send_requests(city)