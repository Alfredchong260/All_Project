import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'Maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = [f'https://www.maoyan.com/board/4?offset={page}' for page in range(0, 91, 10)]

    def parse(self, response):
        dd_lst = response.css('.board-wrapper dd')
        for dd in dd_lst:
            name = dd.css('p.name a::text').get().strip()
            star = dd.css('p.star::text').get().strip()
            releasetime = dd.css('p.releasetime::text').get().strip()
            integer = dd.css('p.score i.integer::text').get().strip()
            fraction = dd.css('p.score i.fraction::text').get().strip()
            score = integer + fraction

            yield MaoyanItem(name=name, star=star, releasetime=releasetime, score=score)

        # next_page = response.xpath('//ul[@class="list-pager"]/li[8]/a/@href').extract()[0]
        # if next_page:
        #     full_url = 'https://www.maoyan.com/board/4' + next_page
        #     yield scrapy.Request(url=full_url, callback=self.parse)
