import time

import requests
import re
import multiprocessing
import concurrent.futures


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


if __name__ == '__main__':
    # for page in range(1, 11):  # 一共有多少个进程  主进程 + 子进程 = 11个进程
    #     url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    #     multiprocessing.Process(target=run, args=(url,)).start()

    start_time = time.time()  # 记录整个进程池池子的执行的执行时间
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for page in range(1, 11):  # 一共有多少个进程  主进程 + 子进程 = 11个进程
            url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
            executor.submit(run, url)

    print('执行时间:', time.time() - start_time)

# 池子模块: 进程任务数量可控
"""
理想状态下:
    进程数量: cpu核数 * 2 + 1
    
"""