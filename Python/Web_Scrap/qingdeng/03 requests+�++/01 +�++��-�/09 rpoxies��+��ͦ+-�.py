import requests


def get_proxy():
    """获取代理"""
    json_data = requests.get(url='http://demo.spiderpy.cn/get/').json()
    proxy = json_data['proxy']

    return proxy

proxy = get_proxy()


proxies = {
    # 以官方文档为准
  "http": "http://" + proxy,
  "https": "http://" + proxy,
}

# proxies  使用代理的关键字, 代理需要构建成上诉字典的形式
# 代理质量不高, 请求会报错(requests.exceptions.ProxyError)
response = requests.get(url='https://www.baidu.com', proxies=proxies)
print(response.text)

