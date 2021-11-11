import requests


def get_proxy():
    """获取代理的函数"""
    proxy = requests.get(url='http://127.0.0.1:5000/get').text
    print('获取到的代理:', proxy)
    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    return proxies


"""用代理请求百度"""
response = requests.get(url='https://www.baidu.com', proxies=get_proxy())
print(response.text)
