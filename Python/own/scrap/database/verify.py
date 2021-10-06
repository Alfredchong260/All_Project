"""
检测模块
    从数据库中把代理数据拿出来，挨个挨个检测代理的可用性(使用多线程来执行)
    可用：设置评分100
    不可用：执行减分操作
"""
from configure import TEST_URL, WORKERS_NUM, TIMEOUT
from database import RedisClient
import concurrent.futures
import requests

REDIS = RedisClient()
success = [200, 201, 202, 203, 204, 205, 206, 301, 302, 307]

def verify(proxy):
    '''
    检测代理的可用性
    :param proxy:需要检测的代理
    '''
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
}

    # 当访问超时2秒时会报错，所以用try语句来捕获错误
    try:
        response = requests.get(url=TEST_URL, proxies=proxies, timeout=TIMEOUT)
        if response.status_code in success:
            # 请求成功，代表代理质量高，可设置成100评分
            print(f'*****代理可用*****\n{proxy}')
            REDIS.max(proxy)

        else:
            # 请求失败，代表代理质量低，执行减分操作
            print(f'#####请求状态码不合法#####\n{proxy}')
            REDIS.decrease(proxy)
    except Exception:

        # 如果try代码快报错，代表当前代理请求超时，代表代理质量低，可进行减分操作
        REDIS.decrease(proxy)
        print(f'---请求超时---\n{proxy}')

def thread_pool():
    """
    线程池检测代理
    """
    # 1. 从数据库中取出代理
    all_proxies = REDIS.all()
    # 2. 用线程池检测代理
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS_NUM) as exe:
        for proxy in all_proxies:
            exe.submit(verify, proxy)

if __name__ == '__main__':
    # 如果有几千个代理，速度会非常慢
    # 多任务，多线程，多进程选择哪一个更好
    # 考虑到资源问题，选择多线程

    # proxy = ['1.196.177.160:6666', '1.169.177.180:2222', '1.196.177.254:6666',
    #         '1.197.203.189:8888', '1.198.73.252:1111', '1.199.31.33:3333']

    # for pro in proxy:
    #     verify(pro)

    thread_pool()
