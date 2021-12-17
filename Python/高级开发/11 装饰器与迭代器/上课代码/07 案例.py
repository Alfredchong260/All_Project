"""
    过滤下列一串网址中不属于猫眼的网址
"""
urls = [
    'https://maoyan.com/board/4?offset=0',
    'https://maoyan.com/board/4?offset=10',
    'https://maoyan.com/board/4?offset=20',
    'https://maoyan.com/board/4?offset=30',
    'https://www.baidu.com',
    'https://www.sohu.com',
    'https://maoyan.com/board/4?offset=40',
    'https://maoyan.com/board/4?offset=50',
]
import requests


def decorator(func):
    """装饰器的固定语法"""
    def wrapper(*args, **kwargs):
        #
        result = func(*args, **kwargs)
        return result

    return wrapper


def filter_url(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        print(kwargs['url'])
        # 如果不是猫眼电影的网址,全部过滤掉
        if 'maoyan' not in kwargs['url']:
            return url, '不是猫眼的地址,不请求'
        result = func(*args, **kwargs)  # 请求服务器,获取数据
        return result

    return wrapper


def download_maoyan(url):
    response = requests.get(url)
    return response.request.url


download_maoyan = filter_url(download_maoyan)
for url in urls:
    # 默认会采集所有的地址
    ret = download_maoyan(url=url)
    print('ret', ret)

"""
    不能修改原有的方法
    
"""
