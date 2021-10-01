import requests
import execjs
import os

id = input('请输入想要下载的歌曲id：')

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'cookie': '_iuqxldmzr_=32; _ntes_nnid=2edf3f388eb4ba5ac1adc384f4edaa50,1629991516323; _ntes_nuid=2edf3f388eb4ba5ac1adc384f4edaa50; NMTID=00OgSmal5VkWr9sNU68vIZx_ik5P1kAAAF7gxC6AQ; WEVNSM=1.0.0; WNMCID=eebttz.1629991516743.01.0; WM_TID=ZsEAzNdZXNpEFFRFEFIqi9BbBwCLoAGc; hb_MA-891C-BF35BECB05C1_source=www.google.com; WM_NI=P85VGaFJZngFQtx625hfEod4LBRfSa6%2F07gupPkJdtkbiGmRo3zvtfgaHYs5OuvkIL%2FOcDeR%2F0%2BXGL%2FvnPCnQKcs5NP9c9Iyu0wA6fKIlRHxQO7HAxDCE%2FDjvWyMP9TSTWI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9d760a3aff892b15c958e8ab7d85f968e9b84f8798392fcb9b76abcb1bcb7c22af0fea7c3b92a94e8fbb7c66b8696968fe64e93acb8d7b13facba8b90e740909e9e87d26bf6f100d8e67fb490a5abe780a9bea7a8f05aadedb697f76ea5bf88baf23f8dabba8ccc48ed91ada5e85aedf0e5b9c648edaaa2b1c2669395ad94b84694e7addacc73b7f0b9a2b56e8997a4b3cb749391f9a9c474889d8bd0c762b689b7aed333988d9cb8cc37e2a3; JSESSIONID-WYYY=ric5EvFXrTUjcz%5CzYjqaSiby8rxZSWskIf%5CpcqS5052qfkpKw3%5CYMBbFwzAqlvk2GObjxHOXH%2BgSQ3aTMEbdfpY%2Fc4ezbXWxrjZvpeCm17%5C7rAx54Mcz994dhsslNZvy6g6FDQJE2srTzxdIjF6s04Qz49h8EaUUvQXF%5CuXw%2BIhyH1Xa%3A1632463998026; playerid=58941602'
}

js = open('./wangyiyun.js', encoding='utf-8').read()
ctx = execjs.compile(js)
result = ctx.call('start', id)

data = {
    'params' : result['encText'],
    'encSecKey': result['encSecKey']
}

response = requests.post(url, headers=headers, data=data)
response = response.json()
# print(response)
url = response['data'][0]['url']
title = response['data'][0]['id']

end = url.split('.')[-1]
content = requests.get(url, headers=headers).content

filename = './music/'

if not os.path.exists(filename):
    os.mkdir(filename)

with open(f"{filename}{id}.{end}", 'wb') as w:
    w.write(content)
