import scrapy

from ..items import Qd07MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = [f'https://www.maoyan.com/board/4?offset={page}' for page in range(0, 91, 10)]

    def parse(self, response):
        # print(response.text)
        dds = response.css('.board-wrapper>dd')  # 所有的dd标签

        for dd in dds:
            name = dd.css('.name a::text').get()
            star = dd.css('.star::text').get().strip()
            releasetime = dd.css('.releasetime::text').get().strip()
            score = dd.css('.score i::text').getall()
            score = ''.join(score)
            yield Qd07MaoyanItem(name=name, star=star, releasetime=releasetime, score=score)