import scrapy

from ..items import Qd01QuotesItem


class QuotesNextSpider(scrapy.Spider):
    name = 'quotes_next'
    allowed_domains = ['toscrape.com']

    # 用列表推导式收集具有规律的网址   start_urls 里面请求的网址只能发送 get 请求
    # start_urls = [f'https://quotes.toscrape.com/page/{page}/' for page in range(1, 11)]

    # start_urls = ['https://quotes.toscrape.com/']

    def start_requests(self):
        """重写start_url"""
        yield scrapy.Request(url='https://quotes.toscrape.com/', callback=self.parse)

    def parse(self, response):
        divs = response.css('.quote')  # 提取所有的 div 标签

        for div in divs:
            info = div.css('.text::text').get()  # 名言警句
            author = div.css('.author::text').get()  # 作者
            tags = div.css('.tags a::text').getall()  # 标签

            yield Qd01QuotesItem(info=info, author=author, tags=tags)

        # 处理翻页
        next_page = response.css('.next a::attr(href)').get()

        # print(next_page)
        if next_page:
            all_url = 'https://quotes.toscrape.com' + next_page  # 拼接完整网址
            # scrapy.Request 构建一个新的请求, 让下载器在互联网中下载资源, 也会返回此次的请求体
            # 返回的请求体会交给 callback 指定的函数处理
            # 构建的请求头也需要通过 yield 返回
            yield scrapy.Request(url=all_url, callback=self.parse)
