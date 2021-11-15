import scrapy


# .. 相对导入
from ..items import Qd01QuotesItem


class QuotesItemSpider(scrapy.Spider):
    name = 'quotes_item'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        divs = response.css('.quote')  # 提取所有的 div 标签

        for div in divs:
            info = div.css('.text::text').get()  # 名言警句
            author = div.css('.author::text').get()  # 作者
            tags = div.css('.tags a::text').getall()  # 标签

            # yield {
            #     'info': info,
            #     'author': author,
            #     'tags': tags,
            # }

            yield Qd01QuotesItem(info=info, author=author, tags=tags)

