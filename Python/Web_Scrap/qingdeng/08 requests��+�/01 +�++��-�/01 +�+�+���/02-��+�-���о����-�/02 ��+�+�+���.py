"""

账号: mb51222353
密码: 123456..

个人中心地址
    https://my.pcbaby.com.cn/user/adminIndex.jsp
"""

import requests


"""模拟登陆"""
headers = {
    'Host': 'passport3.pcbaby.com.cn',
    'Origin': 'https://my.pcbaby.com.cn',
    'Referer': 'https://my.pcbaby.com.cn/login.jsp?return=http%3A%2F%2Fmy.pcbaby.com.cn%2Fuser%2FadminIndex.jsp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

data = {
    'return': 'https://my.pcbaby.com.cn/user/adminIndex.jsp',
    'bindUrl': 'https://my.pcbaby.com.cn/passport/bindMobile.jsp?return=https://my.pcbaby.com.cn/user/adminIndex.jsp',
    'username': 'mb51222353',
    'password': '123456..',
    'auto_login': '30',
    'checkbox': 'on',
}

# 创建一个会话维持对象
session = requests.Session()

# 登陆地址
login_url = 'https://passport3.pcbaby.com.cn/passport3/passport/login_ajax_do_new.jsp?req_enc=UTF-8'

login_response = session.post(url=login_url, data=data, headers=headers)
print(login_response.text)
print(login_response.status_code)
# 登陆成功了
# cadbury

"""会话维持的状态请求个人中心页面"""
my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'

response = session.get(url=my_home_url)

print(response.text)
print(response.status_code)

with open('my_home.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)


"""
vip电影
音乐
...
"""


"""
第三方接口: 破解vip音乐接口
"""

# 抓取用户数据, 需要做登录的话, 那么我们代码也要做模拟登陆
