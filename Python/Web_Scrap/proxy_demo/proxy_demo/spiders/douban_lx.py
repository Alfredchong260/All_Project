import scrapy


class DoubanLxSpider(scrapy.Spider):
    name = 'douban_lx'
    allowed_domains = ['mover.douban.com']
    start_urls = ['http://mover.douban.com/']

    def parse(self, response):
        pass
