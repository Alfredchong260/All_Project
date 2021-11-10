'''
检测模块
'''
from database import RedisClient
from configure import URL
import concurrent.futures
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

Client = RedisClient()

def verify_proxy(proxy):
    '''
    传入一个代理，检测可用性
    '''
    proxies = {
        'http':'http://' + proxy,
        'https':'https//' + proxy
}
    
    try:
        response = requests.get(URL, headers=headers, proxies=proxies, timeout=5)
        if response.status_code == [200, 204, 206, 302]:
            # 如果代理可用，就调用之前写过的数据库类里面的max方法
            print('*****代理可用*****', proxy)
            Client.max(proxy)
        else:
            # 如果请求不成功，代表传进来的代理不可用,就调用数据库类的decrease方法
            print('-----请求状态不可发-----',proxy)
            Client.decrease(proxy)

    except Exception:
        # 如果引发报错，代表代理没有在规定时间内请求到数据，这种情况也将代理是为不可用
        print('请求超时')
        Client.decrease(proxy)

# 检测代理的速度很慢，所以使用多线程
def verify_thread_pool():
    '''线程池检测代理'''
    # 1.从数据库中拿到所有代理
    proxy_list = Client.all()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
        for proxy in proxy_list:
            exe.submit(verify_proxy, proxy)


proxy = '120.0.0.12:5000'
verify_proxy(proxy)
# if __name__ =='__main__':
#     verify_thread_pool()
