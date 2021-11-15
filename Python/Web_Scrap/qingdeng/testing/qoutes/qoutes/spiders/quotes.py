import scrapy

# 相对路径导入
from ..items import QoutesItem


class QuotesSpider(scrapy.Spider):
    # 爬虫文件名字：后续在运行项目的时候需要根据名字运行
    name = 'quotes'
    # 运行项目的时候，请求采取的数据，都会限制在这个域名下，限制的域名是一个列表，后续可添加域名
    allowed_domains = ['toscrape.com']
    # 数据采集的起始网址，是自动生成的，所以一般需要修改
    # 是一个列表，凡是列表里面的网址，后续都会被请求
    # 如果采集的地址有规律，一般会通过列表推导式，推导所有地址

    # 用列表推导式，推导所有地址   start_urls 里面请求的网址只能发送get请求
    start_urls = [f'https://quotes.toscrape.com/page/{page}' for page in range(1, 11)]

    # 用此方法可以用post请求
    # def start_requests(self):
    #     '''重写start_urls'''
    #     yield scrapy.Request(url='http://quotes.toscrape.com/', callback=self.parse)
    #     pass

    def parse(self, response):
        # start_urls 网址中所有的地址，默认会给parse函数处理
        # parse 函数必须有rensponse参数

        # repsonse = 具有所有响应体方法及属性 + 具有之前所学的所有数据解析的方法 <xpath, css, re>
        # print(response.text)
        """
        parse函数主要处理数据的解析
        """
        divs = response.css('.quote')
        for div in divs:
            info = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tag::text').getall()

            # yield {
            #     'info': info,
            #     'author': author,
            #     'tags': tags
            # }

            yield QoutesItem(info=info, author=author, tags=tags)

        # # 处理翻页
        # next_page = response.css('.next>a::attr(href)').get()

        # if next_page:
        #     next_url = 'http://quotes.toscrape.com' + next_page # 拼接完整网址

        #     # 构建一个新的请求，让下载器在互联网下载资源
        #     # 返回的请求体会交给callback指定的函数处理
        #     yield scrapy.Request(url=next_url, callback=self.parse)

"""
如何解决反爬
如何保存数据
框架调用的顺序是什么

# 只能用于测试数据是否正常返回
scrapy crawl quotes -o data.csv
"""
