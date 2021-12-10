import time
import requests
import threading

urls = [
    'https://www.maoyan.com/board/4?offset=0',
    'https://www.maoyan.com/board/4?offset=10',
    'https://www.maoyan.com/board/4?offset=20',
    'https://www.maoyan.com/board/4?offset=30',
    'https://www.maoyan.com/board/4?offset=40',
    'https://www.maoyan.com/board/4?offset=50',
    'https://www.maoyan.com/board/4?offset=60',
    'https://www.maoyan.com/board/4?offset=70',
    'https://www.maoyan.com/board/4?offset=80',
    'https://www.maoyan.com/board/4?offset=90',
]


def download(url, index):
    response = requests.get(url)
    print(response.request.url)
    with open('maoyan.txt', mode='a') as f:
        f.write(f'{index}' + ',' + response.request.url + '\n')


start_time = time.time()
index = 1
# 多线程的作用是将 普通对象 变成 多线程对象
for url in urls:
    # download(url)
    t1_download = threading.Thread(target=download, args=(url, index), kwargs={})
    t1_download.start()
    index += 1

while len(threading.enumerate()) > 1:
    time.sleep(0.1)

print('程序运行的时间:\t', time.time() - start_time)

"""
    多线程执行的顺序不一致 --> 每一个请求执行的时间不一样 电脑的内存,cpu运行速度,网络请求的延时
    能不能让多线程爬取的时候有顺序 ? 不可能
    可以对爬取的结果进行排序
    
    爬虫大部分时间都在等待服务器响应
"""
