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


def download(url):
    response = requests.get(url)
    print(response.request.url)


start_time = time.time()
# 多线程的作用是将 普通对象 变成 多线程对象
for url in urls:
    # download(url)
    # args=(), kwargs=None
    """
    target : 普通对象
    args   : 位置参数 ,需要传递一个元祖
    kwargs : 关键字参数,需要传递一个字典
    """
    t1_download = threading.Thread(target=download, args=(url,), kwargs={})
    t1_download.start()

while len(threading.enumerate()) > 1:
    print('当前程序拥有的线程:', threading.enumerate())
    time.sleep(0.1)

print('程序运行的时间:\t', time.time() - start_time)
