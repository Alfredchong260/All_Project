from database import RedisClient
import requests
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

def proxy_yun():
    '''
    云代理
    '''
    for page in range(1, 11):
        time.sleep(1)
        url = f'http://www.ip3366.net/?stype=1&page={page}'
        print(f'云代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_kuai():
    '''
    快代理
    '''
    for page in range(1,11):
        time.sleep(1)
        url = f'https://www.kuaidaili.com/free/inha/{page}/'
        print(f'快代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_89():
    '''
    89代理
    '''
    for page in range(1, 11):
        time.sleep(1)
        url = f'https://www.89ip.cn/index_{page}.html'
        print(f'89代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_xiaohuan():
    '''
    小幻代理
    '''
    for page in range(1, 11):
        time.sleep(1)
        url = f'https://ip.ihuan.me/?page={page}'
        print(f'小幻代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_ipku():
    '''
    ip库代理
    '''
    for page in range(1, 4):
        time.sleep(1)
        url = f'http://ip.jiangxianli.com/?country=中国&page={page}'
        print(f'ip库代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_xila():
    '''
    xila代理
    '''
    time.sleep(1)
    for page in range(1, 11):
        url = f'http://www.xiladaili.com/gaoni/{page}/'
        print(f'西拉代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_xiaosu():
    '''
    小舒代理
    '''
    time.sleep(1)
    url = 'http://www.xsdaili.cn/dayProxy/ip/2459.html'
    print(f'小舒代理：{url}')
    response = requests.get(url, headers=headers)
    obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
    data = re.findall(obj, response.text)
    for ip, port in data:
        yield ip + ":" + port

def proxy_seofangfa():
    '''
    xiaofangfa代理
    '''
    time.sleep(1)
    url = 'https://proxy.seofangfa.com/'
    print(f'xiaofangfa代理：{url}')
    response = requests.get(url, headers=headers)
    obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
    data = re.findall(obj, response.text)
    for ip, port in data:
        yield ip + ":" + port

def proxy_yqie():
    '''
    yqie代理
    '''
    time.sleep(1)
    url = 'http://ip.yqie.com/ipproxy.htm'
    print(f'yqie代理：{url}')
    response = requests.get(url, headers=headers)
    obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
    data = re.findall(obj, response.text)
    for ip, port in data:
        yield ip + ":" + port

def proxy_freeproxylist():
    '''
    freeproxylist代理
    '''
    time.sleep(1)
    for page in range(1, 11):
        url = f'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}'
        print(f'freeproxylist代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_free():
    '''
    free-proxy-list代理
    '''
    time.sleep(1)
    url = 'https://free-proxy-list.net/'
    print(f'free-proxy-list代理：{url}')
    response = requests.get(url, headers=headers)
    obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
    data = re.findall(obj, response.text)
    for ip, port in data:
        yield ip + ":" + port

def proxy_scan():
    '''
    proxyscan代理
    '''
    time.sleep(1)
    url = 'https://www.proxyscan.io/'
    print(f'proxyscan代理：{url}')
    response = requests.get(url, headers=headers)
    obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
    data = re.findall(obj, response.text)
    for ip, port in data:
        yield ip + ":" + port

def proxy_hideme():
    '''
    hideme代理
    '''
    time.sleep(1)
    for num in range(0, 640, 64):
        url = f'https://hidemy.name/en/proxy-list/?start={num}#list'
        print(f'proxyscan代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port

def proxy_freeproxylists():
    '''
    freeproxylists代理
    '''
    time.sleep(1)
    for page in range(1, 6):
        url = f'https://www.freeproxylists.net/?page={page}'
        print(f'freeproxylists代理：{url}')
        response = requests.get(url, headers=headers)
        obj = re.compile('.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5}).*?', re.S)
        data = re.findall(obj, response.text)
        for ip, port in data:
            yield ip + ":" + port
proxy_list = [proxy_89, proxy_kuai, proxy_xiaohuan, proxy_ipku, proxy_xila, proxy_xiaosu, proxy_seofangfa, proxy_yqie, proxy_freeproxylist, proxy_free, proxy_scan, proxy_hideme, proxy_freeproxylists]

if __name__ == '__main__':

    client = RedisClient()

    # for func in proxy_list:
    #     proxies = func()
    #     for proxy in proxies:
    #         print(proxy)
    #         client.add(proxy)

    result = client.all()
    print(result)
