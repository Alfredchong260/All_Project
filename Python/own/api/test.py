import requests

url = 'https://api.iyk0.com/wzcz'
hero = input('请输入你要查询的英雄：')
param = {
    'msg': hero
}

response = requests.get(url, params=param)
data = response.json()
print(data['data'])
# for i in data['data']:
#     print('英雄详情：{}'.format(i))

# with open('pic.jpg', 'wb') as f:
#     f.write(response.content)
