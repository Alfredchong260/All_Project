import requests


try:
    proxy_response = requests.get('https://www.baidu.com/', timeout=0.0001)
except Exception as e:
    print('正在请求第二次...')
    proxy_response = requests.get('https://www.baidu.com/', timeout=0.0001)

"""
对于报错可以用异常捕获取处理, 可以在异常捕获中进行异常重试

异常重试最好封装函数
"""



