import scrapy

from ..items import Qd02ZzsItem


class ZzsSpider(scrapy.Spider):
    name = 'zzs'
    allowed_domains = ['zhangzishi.com']
    start_urls = [f'https://www.zhangzishi.com/page/{page}' for page in range(1, 37)]

    def parse(self, response):
        articles = response.css('.content article')

        for art in articles:
            title = art.css('h2 a::text').get()
            info = art.css('.note::text').get()
            reads = art.css('.post-views::text').re('\d+')[0]  # 阅读数
            commons = art.css('.post-like span::text').get()  # 点赞数

            yield Qd02ZzsItem(title=title, info=info, reads=reads, commons=commons)

