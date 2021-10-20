# https://image.so.com/i?q=%E9%A3%8E%E6%99%AF&src=srp

# url编码: 默认url中不支持中文, 默认遇到中文会经过url编码
# url编码构成: 百分号 + 字母 + 数字
"""
https://image.so.com/i?q=%E9%A3%8E%E6%99%AF&src=srp

查询参数:
    ? 前面是请求的地址, 后面是一系列的查询参数
    & 分割每一个查询参数

所有的查询参数都是二值型的数据
"""
import requests

url = 'https://image.so.com/i'

params = {
    'q': '风景',
    'src': 'srp'
}
# ? 可加可不加
response = requests.get(url=url, params=params)
print(response.request.url)


"""url编码问题"""
# # url编码: 默认url中不支持中文, 默认遇到中文会经过url编码
# # url编码构成: 百分号 + 字母 + 数字
# requests.utils.quote 对中文进行编码
print(requests.utils.quote('风景'))
# requests.utils.unquote 对中文进行解码
print(requests.utils.unquote('%E9%A3%8E%E6%99%AF'))

