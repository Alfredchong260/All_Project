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

url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'

response = requests.get(url)
data = response.json()
json_data = json.dumps(data)
print(data)

with open('data.json', 'w', encoding='utf-8') as w:
    w.write(json_data)
