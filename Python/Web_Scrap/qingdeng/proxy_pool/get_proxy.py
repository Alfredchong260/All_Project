import requests

def get_proxy():
    proxy = requests.get('http://127.0.0.1:5000/get')
    print('获取到的代理', proxy.text)
    proxies = {
        'http':"http://" + proxy.text,
        'https':'https://' + proxy.text,
}

    return proxies

response = requests.get('https://www.baidu.com', proxies=get_proxy())
print(response.text)
