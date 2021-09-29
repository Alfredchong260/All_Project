# 定义
dict1 = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75
}

dict2 = {
    'sex': '女',
    "height": 1.80
}

# 合并<更新>字典: dict2 合并到 dict1 里面, 如果有相同的键值对, 键值对会覆盖
# dict1.update(dict2)
# print(dict1)

print(dict1.keys())  # .keys() 取字典的所有键
print(dict1.values())  # .values() 取字典的所有值
print(dict1.items())  # .items() 取字典的所有键值对

# 遍历字典的键与值
for k, v in dict1.items():
    print(k, v)
