"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	
	要求：
		1、请求上述网址的数据
		2、把获取到的数据保存到json文件中
            文件命名: data.json
            需要在文件中看到json字符串
			
请在下方编写代码
"""
import requests
import json


response = requests.get(url='https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76')
json_data = response.text
# print(type(response.json()))

# 序列化   对象 --> 字符串
json_str = json.dumps(json_data, ensure_ascii=False)
print(type(json_str))

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_data)

# 为什么要保存json
"""
需求:
    数据
    
    用途: 
        网站的数据显示<假数据>, json 
        MongoDB 数据库  --> 非关系型数据库<类似字典>
        爬虫: 很多情况下, 抓取的数据并不是具有规范的格式的, 团队开发
    
"""
