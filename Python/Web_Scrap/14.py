'''
    scrapy是一个一场处理框架

分为六大组件
engine                      引擎
item                        项目
scheduler                   调度器
dowmloader                  下载器
spiders                     爬虫
item pipeline               管道
downloader middlewares      下载在中间件
spider middlewares          爬虫中间件
'''

"""
engine 打开一个网站，请求第一个需要爬取的url
engine 从spider中获取第一个要爬取的url,使用scheduler以requests的形式调度
engine向scheduler请求下一个需要爬取的url
"""

'''
item：定义一个item数据结构
pipeline：数据存放的地方
middlewares：爬虫中间件和下载中间件
spiders：爬虫的实现
setitngs：项目的全局配置
'''

"""
name：项目唯一的名字，用来区分不同的spider
allowed_domains：它是允许爬取的域名，如果初始或后续的请求链接，不是在这个域名下，则请求链接会被过滤掉
start_urls：它包含了spider在启动时爬取的url列表,初始的请求是由它来定义的
parse：它是spider的一个方法，start_url请求会构成一个响应，这个响应会作为一个参数传递给parse函数，parse负责解析响应并获取数据
"""

'''
item：是一个保存爬取数据的容器，它的使用方法和字典类似，相比字典item多了保护机制
      可以避免拼写错误或文字错误
'''

"""
解析response
parse()方法的参数response是start_url里面的链接爬取后的结果，可以在parse方法中直接对response变量包含的内容进行解析
"""

'''
想到获取下一页，那么需要使用
scrapy.Request
需要传入两个参数
url：请求链接
callback：回调函数，引擎会将下一页的响应返回给这个回调函数，回调函数可以解析或
    生成下一个请求，回调
'''
