"""
    将原来的代码使用装饰器改成多线程逻辑
"""
import threading
import time

import parsel
import requests

urls = [
    'https://maoyan.com/board/4?offset=0',
    'https://maoyan.com/board/4?offset=10',
    'https://maoyan.com/board/4?offset=20',
    'https://maoyan.com/board/4?offset=30',
    'https://maoyan.com/board/4?offset=40',
    'https://maoyan.com/board/4?offset=50',
    'https://maoyan.com/board/4?offset=60',
    'https://maoyan.com/board/4?offset=70',
    'https://maoyan.com/board/4?offset=80',
    'https://maoyan.com/board/4?offset=90',
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}


def decorator(func):
    def wrapper(*args, **kwargs):
        # print(func, args, kwargs)
        # func(*args, **kwargs)
        # 多线对象是没有返回值的
        t1 = threading.Thread(target=func, args=args, kwargs=kwargs)
        t1.start()

    return wrapper


# @decorator
def download(url):
    response = requests.get(url, headers=headers)
    sel = parsel.Selector(response.text)
    title = sel.css('.name a::text').get()
    # print(url, title)
    # 如果是有返回值应该怎么处理 ?
    return url, title  # 函数是有返回值的


def save(url, title):
    open(title + '.txt', mode='w').write(url)


@decorator
def proxy_download(url):
    url2, title = download(url)
    print(url2, title)
    save(url2, title)


for url in urls:
    # url2, title = download(url)
    # print(url2, title)
    # save(url2, title)

    proxy_download(url)
    # t1 = threading.Thread(target=download, args=(url,))
    # t1.start()
