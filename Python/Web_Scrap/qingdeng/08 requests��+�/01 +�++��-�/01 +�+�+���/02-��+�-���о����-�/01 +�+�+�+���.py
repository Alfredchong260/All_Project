"""

账号: mb51222353
密码: 123456..

个人中心地址
    https://my.pcbaby.com.cn/user/adminIndex.jsp
"""

import requests

my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

response = requests.get(url=my_home_url, headers=headers)

print(response.text)
print(response.status_code)

with open('my.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)


