import requests

session = requests.Session()

url = 'http://159.75.114.202:8000/getCaptcha?0.34585059820270647'

cookies = {
    'Cookie': 'session=eyJjb2RlIjoiNDAxOCJ9.YXanzg.2KNDw7dhWvWZlxmSv-_-ztS0oOo'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response = session.get(url, headers=headers, cookies=cookies)

with open('yzm.jpg', 'wb') as w:
    w.write(response.content)

print('验证码下载完成')

cookies_jar = response.cookies.get_dict()
print(cookies_jar)

code = input('请输入验证码：')

register = 'http://159.75.114.202:8000/register'

json_data = {
    'captcha': code,
    'password': "123456",
    'phone': "15645455252"
}

register_res = session.post(url=register, json=json_data, cookies=cookies, headers=headers)
print(register_res.json())
