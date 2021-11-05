# 1. 找数据所对应的地址
# import csv
#
# import parsel
# import requests
#
# url = 'https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90'
#
# # 2. 请求地址数据
# response = requests.get(url=url)
# html_data = response.text
# # print(html_data)
#
# # 3. 数据解析
# # 3.1 转换数据类型
# selector = parsel.Selector(html_data)
# # 3.2 解析数据
# lis = selector.css('.g-doctor-items.to-margin ul li')  # 所有li
#
# for li in lis:
#     doctor_name = li.css('.wrap>a::text').get()
#     doctor_lever = li.css('dl dt::text').getall()[1].strip()
#     doctor_kind = li.css('dd p:nth-child(1)::text').get()
#     doctor_beloging = li.css('p:nth-child(2) .g-txt-ell::text').get()
#     doctor_see_price = li.css('.infos.video span em:nth-child(2)::text').get().strip()
#
#     print(doctor_name, doctor_lever, doctor_kind, doctor_beloging, doctor_see_price)
#     with open('唯医网.csv', mode='a', encoding='utf-8', newline='') as f:
#         csv_write = csv.writer(f)
#         csv_write.writerow([doctor_name, doctor_lever, doctor_kind, doctor_beloging, doctor_see_price])
import csv

import parsel
import requests
import threading

lock = threading.Lock()


def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url=url)
    return response.text


def parse_data(html):
    """数据解析函数, 传入数据进行解析"""
    selector = parsel.Selector(html)
    lis = selector.css('.g-doctor-items.to-margin ul li')

    data_list = []  # 收集解析出来的数据, 二维列表
    for li in lis:
        doctor_name = li.css('.wrap>a::text').get()
        doctor_lever = li.css('dl dt::text').getall()[1].strip()
        doctor_kind = li.css('dd p:nth-child(1)::text').get()
        doctor_beloging = li.css('p:nth-child(2) .g-txt-ell::text').get()
        doctor_see_price = li.css('.infos.video span em:nth-child(2)::text').get().strip()

        data_list.append([doctor_name, doctor_lever, doctor_kind, doctor_beloging, doctor_see_price])

    return data_list


def save_data(data):
    lock.acquire()
    with open('唯医网.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data)
        print(data)
    lock.release()

# 转换函数对象，只针对一个函数任务才能转换
# 可以定义一个主函数，去吧其他函数任务的逻辑在主函数实现
def run(url):
    """主函数, 调用其他函数任务执行"""
    # 1. 调用发送网络请求的方法
    html_data = send_requests(url)
    # 2. 调用数据解析的方法, 得到二维列表
    data_list = parse_data(html_data)
    for data in data_list:
        # 3. 调用数据保存的方法
        save_data(data)

# run('https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90')

for page in range(1, 11):
    url = f'https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90/p{page}'
    threading.Thread(target=run, args=(url,)).start()
