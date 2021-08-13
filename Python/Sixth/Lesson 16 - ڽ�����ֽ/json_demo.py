# 将台服的英雄数据保存到txt文档中 文档的名字命名为  英雄.json结尾

# 向目标地址发送请求并获得数据响应
import requests

url = 'https://ddragon.leagueoflegends.com/cdn/11.6.1/data/zh_TW/champion.json'
header = {
    # 请求头部信息
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
response = requests.get(url, headers=header)
# print(type(header))
# result = response
# print(result)
# 当结果为 [200] 代表目标网站的反爬虫处理没有被激活

json_data = response.text
# print(json_data)

# 将数据进行取舍   name，id，title，blurb(描述)
import json

# 将数据转换成字典类型
dc_data = json.loads(json_data)
# print(dc_data)
data = dc_data['data']
# print(data)

# 新建一个列表保存数据
lst_data = []

# 通过英雄的title去里面的value
for i in data:
    lst_data.append(i)
# 检查爬取的数据数量是否正确
print(len(lst_data))

# 通过英雄的title取里面的value
lol_data = []
for title_name in data:
    name = data[title_name]['name']
    id = data[title_name]['id']
    title = data[title_name]['title']
    blurb = data[title_name]['blurb']
    lst = [name, id, title, blurb]
    lol_data.extend(lst)

# 保持英雄的数据
with open('lol_hero_data.txt', mode='w', encoding='utf-8') as w_hero:
    for i in lol_data:
        w_hero.write('\n')
        for j in i:
            w_hero.write(j)
