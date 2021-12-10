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
for url in urls:
    # threading.Thread 子线程
    t1_download = threading.Thread(target=download, args=(url, index), kwargs={})
    # 设置为守护线程 当主线程运行完时 子线程被 kill 掉
    t1_download.setDaemon(True)  # 强制关机 重启程序
    t1_download.start()
    index += 1

# 程序只能运行 0.5 秒钟
# while len(threading.enumerate()) > 1:
#     time.sleep(0.1)
time.sleep(0.6)

print('程序运行的时间:\t', time.time() - start_time)
# 主线程结束掉了

"""
    同步: 顺序执行
    异步: 交叉完成任务,看起来是同时做很多事情(实现的方式有 多线程/多进程/协程)
"""
