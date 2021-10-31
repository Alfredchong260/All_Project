import requests

proxy_response = requests.get('https://www.baidu.com/', timeout=0.0001)
proxy = proxy_response.json()
print(proxy)

"""
requests.exceptions.ConnectTimeout  ; 连接超时
timeout : 指定请求需要在多久返回数据, 超过时间会报错
"""


