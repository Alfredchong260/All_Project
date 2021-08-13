import requests
import json
# 如果没有该模块 取pip下载    不能的话去 csdn 找相关的博客下载
import jsonpath as js
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/'
                      '537.36'}
response = requests.get(url,headers=head)
json_data = response.text
dc_data = json.loads(json_data)
city_name = js.jsonpath(dc_data,'$..name')
city_id = js.jsonpath(dc_data,'$..id')
city_data = {}
count = 0
for i in city_name:
    name = city_name[count]
    id = city_id[count]
    count+=1
    city_data.setdefault(name)
    city_data[name] = id
print(city_data)

# key = []
# value = []
# for i in city_data:
#     key.append(i)
# for i in city_data:
#     value.append(city_data[i])
# print(key)
# print(value)



with open('city_data.txt',mode='a',encoding='utf-8') as city:
    for i in city_data:
        city.write(i + ':' + str(city_data[i]))
        city.write('\n')

