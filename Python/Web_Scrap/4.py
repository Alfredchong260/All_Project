import requests 
from lxml import etree

# 请求数据
# response = requests.get('https://baidu.com/')

# print(type(response))
# #  打印状态码
# print(response.status_code)

# # 网页的源代码
# print(response.text)

# print(type(response.text))
# json和str类型是非常相似的

# 获取cookies
# print(response.cookies)

# 提交数据
# post
# r = requests.head('http://httpbin.org/get')

# 可以删除数据
# r = requests.delete('http://httpbin.org/delete')
# print(r.text)

# get post put delete head options


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
    # 'cookie': '_uuid=E2CA7512-ADFD-7A49-4BE6-77B7D9359BC029307infoc; buvid3=E9C519D2-94D0-4F31-8EC6-D7E01C74F2D9148819infoc',
    # 'referer': 'https://www.bilibili.com/'
}

# data = {
#     'name': 'kk',
#     'age' : 28
# }

# r = requests.get(url, headers=headers)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
# print(r.text)

# 抓取图片
# r = requests.get('https://i0.hdslb.com/bfs/sycp/creative_img/202108/a1ea723ac61d616a46919bfaa7fb95ce.jpg@412w_232h_1c')

# 图片是二进制的数据，转换为str类型
# Byte 
# print(r.content)

# url = 'https://i0.hdslb.com/bfs/sycp/creative_img/202108/624b1873e9da17dbadba037b673c2cd0.jpg@880w_388h_1c_95q'

# r = requests.get(url, headers=headers)
# print(r)
# with open('1.jpg', 'wb') as f:
#     f.write(r.content)

# data = {'name': 'xiaoming', 'age': '30'}
# r = requests.post('http://httpbin.org/post', data)
# print(r.text)


# 响应
# r = requests.get('https://www.bilibili.com/')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)



# 正则表达式
# re.match函数
# 从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功，match()返回none
# pattern：匹配的正则表达式
# string：要匹配的字符串
# flags：标志位，用于控制正则表达式的匹配方式，是否区分大小写，多行匹配
# print(re.match('www', 'www.baidu.com/'))
# \w  匹配字母，数字，下划线
# \W 匹配不是字母，数字，下划线
# .* 通用匹配
# 贪婪匹配，非贪婪匹配
# content = 'hello 123 4567 rea word'
# ^代表头 $代表尾
# 尾可以不标识
# result = re.match('^h.*rea', content)
# print(result)

url = 'https://bilibili.com/'

response = requests.get(url, headers=headers).text
html = etree.HTML(response)
a = html.xpath('//*[@id="primaryChannelMenu"]/span/div/a/span/text()')
print(a)
