# import requests
# 模块.方法
# response = requests.get('http://www.baidu.com')
# print(response)

# 从模块里面导入一个方法
from requests import get
from qd05 import check_login

response = get('http://www.baidu.com')
print([response.text])

# 从模块.模块 导入 方法
# get 是封装了 request 的
from requests.api import get, request

response = get('http://www.baidu.com')
print([response.text])
response = request('get', 'http://www.baidu.com')
print([response.text])

"""
    get 
    post    --> request('get', )
    delete 
    
    requests request
"""

check_login('zhengxin', '123456')
check_login(u_name='zhengxin', pwd='123456')
