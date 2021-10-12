
# requests 模块, 数据请求的模块, 第三方模块<需要我们自行安装>/内置模块<解释器本身自带的模块>
import requests  # 导入模块

# response 响应体对象.  请求和响应
# get 是一种请求方式, post put delete options...(get post)
response = requests.get('https://www.baidu.com/')
print(response)

# 只要是对象就具有对象的属性和方法
# .text   获取Response对象的文本内容
print(response.text)

"""
爬虫项目<案例>实现的步骤:
1. 找数据所对应的地址< url(统一资源定位符) >  系统分析网页性质 <静态数据/动态数据>
2. 请求地址数据(文本, js数据, 图片数据, css数据...)
3. 数据解析, 解析你想要的数据, 剔除不想要的数据(css选择器, xpath节点提取, 正则表达式)
4. 数据的保存 (本地文件<txt,Excel,json...>, 数据库)
"""