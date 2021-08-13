import urllib.request 

response = urllib.request.urlopen('https://www.baidu.com/')

# print(response.read().decode('utf-8'))
# print(response.getheader('Set-Cookie'))
# print(response.readinto('headers'))

# 包含了read(), readinto(), getheader(name), getheaders()

# getheaders是返回所有头的信息
# getheader是返回参数的头信息

# msg, status, reason
# msg返回的是，是否正常访问方绽
# status返回的是，访问网站的状态码
# reason

# status 200：正常访问      403：拒绝访问       404：服务器不存在

# print(response.msg)


# data参数
import urllib.parse
import urllib.request

# data = bytes(urllib.parse.urlencode({'say': 'hello', 'today':'August'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)

# print(response.read().decode('utf-8'))

# 用byte对say hello进行转码，其中使用urllib.parse.urlencode将字典装换为字字符串
# 传递进去的值保存在form{}
# 这个作用是将数据使用post的方式传递到对方服务器
# get 获取数据 post 提交数据

# urllib只是用来了解基本知识
# 提交数据是并不会用到urllib

# timeout 是设置一个超时时间，当访问时间超过timeout设置的时间，就会发生错误

# response = urllib.request.urlopen('https://github.com/', timeout=0.8)
# print(response)


# request 方法的使用
# url = 'https://bilibili.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# dict = {'name': 'k'}

# requ = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(requ)
# print(response.read().decode('utf-8'))


# urlparse()
# 实现url的识别和分段
# from urllib.parse import urlparse

# result = urlparse('https://baidu.com/')
# print(result)


# urlsplit()
# 和urlparse方法类似，但不止解析parse这一部分

# from urllib.parse import urlsplit

# results = urlsplit('https://baidu.com/')
# print(results)


# urljoin()
# 可以做到链接的合并
# urljoin会对传入的两个参对进行连接
from urllib.parse import urljoin

print(urljoin('https://baidu.com', 's?ie=utf-8&wd=python'))
print(urljoin('https://baidu.com', '?category=2#comment'))



# robots 协议
# robots协议， 也称爬虫协议，机器人协议
# 高数爬虫和搜索引擎哪些页面可以抓取，哪些页面不可以抓取

'''
User-agent:*
DIsallow:
Allow:/public/
就是一个协议，但是这个可以不遵守
'''

