import json  # 内置模块

data = {
    'name': '山禾',
    'shares': 100,
    'price': 542.23
}

"""
默认情况下, json的序列化操作如果遇到了中文, 那么会把中文经过Unicode编码
ensure_ascii=False  不使用Unicode编码
"""
data_str = json.dumps(data, ensure_ascii=False)

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(data_str)




