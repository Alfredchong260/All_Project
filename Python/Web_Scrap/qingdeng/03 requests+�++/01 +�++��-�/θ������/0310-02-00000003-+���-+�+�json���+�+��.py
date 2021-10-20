"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	发送 GET 请求

	要求：
		1、请求上述网址的数据
		2、按照要求提取以下字段信息
			title、
			picPath、
			playUrl
		提取下来用 print() 函数打印即可
请在下方编写代码
"""

import requests
import pprint

url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
response = requests.get(url)
json_data = response.json()
# print(json_data)

# 注意数据类型
# print(type(json_data))  # json() 会在底层执行的时候会把字符串转换成对象

pprint.pprint(json_data)

data_list = json_data['data']  # list
# print(data_list)

# for data in data_list:  # 遍历列表里面的字典
#     title = data['title']
#     picPath = data['picPath']
#     playUrl = data['playUrl']
#
#     print(title, picPath, playUrl, sep=' | ')

for data in range(0, len(data_list)):  # 遍历列表的索引
    title = data_list[data]['title']
    picPath = data_list[data]['picPath']
    playUrl = data_list[data]['playUrl']

    print(title, picPath, playUrl, sep=' | ')


# 编写
# 项目
# 变量的命名, 每一个变量名, 都不要重复, 因为变量的值可能会覆盖
# 也不要把自己搞迷糊
