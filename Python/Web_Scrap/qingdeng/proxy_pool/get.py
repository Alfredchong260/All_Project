from database import RedisClient
import concurrent.futures
from concurrent.futures import as_completed
import requests
import time
import re

Client = RedisClient()

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)

def crawler(url):
    print(f'目标网站为：{url}')
    proxies = []
    data = requests.get(url, headers=headers).text
    ip_port = re.findall(obj, data)
    for ip, port in ip_port:
        proxies.append(ip + ':' + port)
    time.sleep(2)

    return proxies


def yun_crawler(exe):
    '''
    捉取云代理数据
    目标网站:'http://www.ip3366.net/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'http://www.ip3366.net/?stype=1&page={page}'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def crawler89(exe):
    '''
    捉取89代理数据
    目标网站:'https://www.89ip.cn/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'https://www.89ip.cn/index_{page}.html'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def kuai_crawler(exe):
    '''
    捉取快代理数据
    目标网站:'https://www.kuaidaili.com/free/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'https://www.kuaidaili.com/free/inha/{page}/'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def xiaohuan_crawler(exe):
    '''
    捉取小幻代理数据
    目标网站:'https://ip.ihuan.me/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'https://ip.ihuan.me/?page={page}'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def xila_crawler(exe):
    '''
    捉取西拉代理数据
    目标网站:'http://www.xiladaili.com/gaoni/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'http://www.xiladaili.com/gaoni/{page}/'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def mipu_crawler(exe):
    '''
    捉取米扑代理数据
    目标网站:'http://proxy.mimvp.com/freeopen?proxy=out_socks'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'http://proxy.mimvp.com/freeopen?proxy=out_socks&sort=&page={page}'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def nima_crawler(exe):
    '''
    捉取泥马代理数据
    目标网站:'http://www.nimadaili.com/gaoni/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'http://www.nimadaili.com/gaoni/{page}/'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

def free_proxy_world_crawler(exe):
    '''
    捉取免费代理网代理数据
    目标网站:'https://www.freeproxy.world/'
    '''
    proxies = []
    for page in range(1, 6):
        url = f'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}'
        proxy = exe.submit(crawler, url)
        proxies.append(proxy)

    return proxies

# 豌豆代理没有端口，由于crawler函数同时爬取端口和ip,所以爬豌豆时会报错
# def wandou_crawler(exe):
#     '''
#     捉取豌豆代理数据
#     目标网站:'https://h.wandouip.com/'
#     '''
#     proxies = []
#     for page in range(1, 6):
#         url = f'https://h.wandouip.com/?page={page}#sec3'
#         proxy = exe.submit(crawler, url)
#         proxies.append(proxy)

#         return proxy

proxies_list = [yun_crawler, crawler89, kuai_crawler, xiaohuan_crawler, xila_crawler, mipu_crawler, nima_crawler, free_proxy_world_crawler]

if __name__ == '__main__':

    # 鸭子类型： 不关注对象是什么类型，只关注对象的行为
    # 创建一个多线池对象，带入函数内部使用
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
        for func in proxies_list:
            # 捕捉连接错误，当发生连接错误，等待两秒后重新尝试
            try:
                proxies = func(exe)
                for proxy in as_completed(proxies):
                    for i in proxy.result():
                        print(i)
                        Client.add(proxy=i)
            except ConnectionError:
                time.sleep(2)
                proxies = func(exe)
                for proxy in as_completed(proxies):
                    for i in proxy.result():
                        print(i)
                        Client.add(proxy=i)
