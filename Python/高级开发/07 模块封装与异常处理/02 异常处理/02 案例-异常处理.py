from requests import get

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

response = get('http://www.baidu.com', headers=headers)
print(response)

"""
    先看错误的信息
    再看错误出现的位置
        先看自己代码的错误
        再看官方源码的错误
"""

data = "{'name':'正心'}"
data_dict = {'name': '正心'}
import json

# print(json.loads(data))  # 代码的报错,与自己的感觉
print(json.loads("""{"name":"正心"}"""))  # 代码的报错,与自己的感觉
