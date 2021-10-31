
import json  # 内置模块

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# json数据本身是字符串
"""
josn 序列化操作:  把对象转换成json字符串
"""
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

"""
json反序列化操作: 把json字符串转换成一个对象
"""
json_dict = json.loads(json_str)

print(json_dict)
print(type(json_dict))