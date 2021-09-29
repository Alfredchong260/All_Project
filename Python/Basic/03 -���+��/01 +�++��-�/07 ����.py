# 字典是一种可变的、无序的、键值对的、复杂的数据容器

# {}  dict

dict1 = {
    'name': '小明',
    'age': 18,
    'hobby': ['吃', '喝', '玩'],
    # 'hobby': ['吃', '喝'],
}

print(dict1)
print(type(dict1))

# 字典取值
# 字典是无序的  不能用索引取值,  需要根据字典的键, 取对应的值<键必须唯一>
print(dict1['name'])
print(dict1['hobby'])

# 字典是可变的
dict1['age'] = 20
# 如果字典中没有这个键, 那么会自动创建
dict1['gender'] = '男'

dict1['hobby'].append('乐')
print(dict1)

# 字典取值键不存在, 会报错
# print(dict1['get'])
# get()  方法, 如果取的键存在, 会取出键的值, 如果没有键不存在, 返回None, 不会报错
print(dict1.get('get'))