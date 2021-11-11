# http://159.75.114.202:8000/

import requests


# 创建一个会话维持对象, 可以直接用此对象发送多次请求, 多次的请求具有状态的维持
session = requests.Session()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
cookies = {'Cookie': 'session=eyJjb2RlIjoiMDgyNSJ9.YXamAg.7iZaCHoTnAaaRONl4NMnuxckEa0'}

yzm_url = 'http://159.75.114.202:8000/getCaptcha?0.6448714205070494'
response = session.get(url=yzm_url, headers=headers, cookies=cookies)
cookies_jar = response.cookies.get_dict()
yzm_data = response.content

with open('yzm.jpg', mode='wb') as f:
    f.write(yzm_data)
print('图片保存完毕...')


"""对接打码平台, 自动识别验证码"""
# code = input('请输入验证码:')
from img_api import base64_api

code = base64_api('yzm.jpg')
print('验证码识别的结果: ', code)


register_url = 'http://159.75.114.202:8000/register'

json_data = {
    'captcha': code,
    'password': "123456",
    'phone': "15645455252"
}

register_response = session.post(url=register_url, json=json_data)
print(register_response.json())


