


"""json数据"""
"""
功能: 目前前后端主流的数据交换格式
形式: 字符串, 外层 {} [] 包裹, 内层嵌套数据, 规范json数据中字段用双引号包裹
    {"字段1": 值1, 字段2:{嵌套字段1: 嵌套值1, 嵌套字段2: [{},{},{}]}}
    和字典很像
    
在json数据中, 字段值必须是一下的数据类型:
    字符串
    数字
    对象(嵌套数据)
    数组
    布尔值
    null   # 表示空
"""

"""
# json数据在用 json() 方法提取之前, 数据类型是字符串
# 用 json() 提取以后, 会在方法底层经过数据类型的转换, 转换成一个对象
"""

import requests


response = requests.get('https://news.163.com/special/yaowen_channel_api/?callback=channel_callback&date=0120')
# data = response.json()
# print(type(data))
# print(data)


# 在数据不是规范的json情况下, 需要用 text 提取数据
data = response.text  # text 获取对象文本数据
print(type(data))
print(data)

# 数据持久化,
