'''
使用代理
'''
import requests

def get_proxy():
    response = requests.get(url='http://127.0.0.1:5000/get').text
    print(f'获取到的代理：{response}')

    proxies = {
        'http': f'http://{response}',
        'https': f'https://{response}'
}
    print(f'构建好的代理：{proxies}')

    return proxies

proxy = get_proxy()

response = requests.get(url='https://www.baidu.com', proxies=proxy)
print(response)
