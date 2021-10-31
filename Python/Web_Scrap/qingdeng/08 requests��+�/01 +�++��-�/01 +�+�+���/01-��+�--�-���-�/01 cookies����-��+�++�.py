# http://159.75.114.202:8000/

import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
cookies = {'Cookie': 'session=eyJjb2RlIjoiMDgyNSJ9.YXamAg.7iZaCHoTnAaaRONl4NMnuxckEa0'}

"""保存验证码图片"""
# 验证码地址, (图片)
yzm_url = 'http://159.75.114.202:8000/getCaptcha?0.6448714205070494'

response = requests.get(url=yzm_url, headers=headers, cookies=cookies)

# 通过响应体对象, 拿到cookies信息
cookies_jar = response.cookies.get_dict()
print('拿到的cookies字段:',cookies_jar)

yzm_data = response.content


with open('yzm.jpg', mode='wb') as f:
    f.write(yzm_data)
print('图片保存完毕...')

"""手动输入验证码"""
code = input('请输入验证码:')

"""发送模拟注册的请求"""
register_url = 'http://159.75.114.202:8000/register'

json_data = {
    'captcha': code,
    'password': "123456",
    'phone': "15645455252"
}

register_response = requests.post(url=register_url, json=json_data, headers=headers, cookies=cookies_jar)
print(register_response.text)


"""
这两次请求, 我们携带上了cookies字段, 保证是同一个用户发送的请求
"""


