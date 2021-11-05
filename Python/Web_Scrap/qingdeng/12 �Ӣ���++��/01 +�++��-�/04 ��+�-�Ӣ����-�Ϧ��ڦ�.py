import time
import requests
import re
import threading
import multiprocessing


def send_requests(url):
    response = requests.get(url=url)
    return response

def parse_data(html):
    result_list = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html, re.S)
    return result_list  # 返回图片地址  --- 列表

def save_data(file_name, data):
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('保存完成:', file_name)

def run(url):
    html_data = send_requests(url).text
    img_Url_list = parse_data(html_data)

    for img_Url in img_Url_list:  # 遍历图片地址
        img_data = send_requests(img_Url).content  # 请求的图片数据
        file_name = img_Url.split('/')[-1]  # 文件名
        save_data(file_name, img_data)

    # print('执行时间:', time.time() - start_time)

# 测试主函数
# run('https://fabiaoqing.com/biaoqing/lists/page/')
# start_time = time.time()

if __name__ == '__main__':
    # 此方式无法控制进程的执行数量, 数据极有可能缺失 ,可以通过池子模块控制进程的执行数据量
    for page in range(1, 11):  # 一共有多少个进程  主进程 + 子进程 = 11个进程
        url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
        multiprocessing.Process(target=run, args=(url,)).start()

"""
多进程无法记录每个进程最终的执行时间
后续可以用池子模块, 记录池子运行的时间
"""
