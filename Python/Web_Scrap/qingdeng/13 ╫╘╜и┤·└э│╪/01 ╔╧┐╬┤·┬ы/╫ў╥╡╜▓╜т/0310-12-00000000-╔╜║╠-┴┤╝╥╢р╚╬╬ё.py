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
import csv
import concurrent.futures
import parsel
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url=url, headers=headers)
    return response.text


def parse_data(data):
    selector = parsel.Selector(data)
    lis = selector.css('.clear.LOGCLICKDATA')

    data_list = []  # 数据的二维列表
    for li in lis:
        room_title = li.css('.title a::text').get()  # 二手房标题
        room_address = li.css('.positionInfo a::text').getall()  # 二手房地址
        room_address = ','.join(room_address)

        room_introduce = li.css('.houseInfo::text').get()  # 二手房型简介
        room_follow = li.css('.followInfo::text').get()  # 关注人数及发布时间
        room_totalPrice = li.css('.unitPrice span::text').get()  # 单价
        room_unitPrice = li.css('.totalPrice.totalPrice2 span::text').get() + '万元'  # 总价

        print(room_title, room_address, room_introduce, room_follow, room_totalPrice, room_unitPrice)
        data_list.append([room_title, room_address, room_introduce, room_follow, room_totalPrice, room_unitPrice])

    return data_list


def save_data(data_list):
    for data in data_list:
        with open('链家.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(data)


def run(url):
    html_data =send_requests(url)
    data_list = parse_data(html_data)
    save_data(data_list)


# 测试主函数是否能运行
# run('https://cs.lianjia.com/ershoufang/pg2/')


if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for page in range(1, 101):
            url = f'https://cs.lianjia.com/ershoufang/pg{page}/'
            executor.submit(run, url)
