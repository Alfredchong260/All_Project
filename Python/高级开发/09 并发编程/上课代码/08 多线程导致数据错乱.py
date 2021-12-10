import time
import random
import requests
import threading

# 1. 创建一把线程锁
lock = threading.Lock()
urls = [
    'https://www.maoyan.com/board/4?offset={}'.format(page) for page in range(1000)  # 1000条数据
]


def download(url, index):
    # response = requests.get(url)
    # print(response.request.url)
    time.sleep(random.random())
    lock.acquire()  # 2. 加锁
    with open('maoyan.txt', mode='a') as f:
        f.write(f'{index}' + ',' + url + '\n')
    lock.release()  # 3. 释放锁  如果不释放,就是死锁
    """每一条线程都可能进行的操作
        1. 打开文件
        2. 写入内容
        3. 关闭文件,保存修改
        
       一千个线程同时进行修改,就会导致错乱
        解决办法
            1. 只允许同时一个人修改文件(加锁)
            2. 利用队列的等其他线程安全工具存储数据
    """


start_time = time.time()
index = 1
for url in urls:
    t1_download = threading.Thread(target=download, args=(url, index), kwargs={})
    t1_download.start()
    index += 1

print('程序运行的时间:\t', time.time() - start_time)
