import scrapy
from book.items import BookItem
import time


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://book.suning.com/']

    def parse(self, response):
        # 大分类分组
        infos = response.xpath('//div[@class="menu-list"]/div[@class="menu-item"]')
        for info in infos:
            item = BookItem()
            item['titles'] = info.xpath('./dl/dt/h3/a/text()').get()

            a_li = info.xpath('./dl/dd/a')
            for a in a_li:
                item['subs'] = a.xpath('./text()').get()
                item['links'] = a.xpath('./@href').get()
                time.sleep(0.05)

                if item['links'] is not None:
                    yield scrapy.Request(
                        item['links'],
                        callback=self.parse_book_list,
                        meta={'item': item}
                    )

    def parse_book_list(self, response):
        item = response.meta['item']
        infos = response.xpath('//ul[@class="general clearfix"]/li')
        for info in infos:
            time.sleep(0.05)
            item['book_name'] = info.xpath('.//a[@class="sellPoint"]/img/@alt').get()
            time.sleep(0.05)
            item['book_img'] = 'https:' + info.xpath('.//a[@class="sellPoint"]/img/@src').get()
            time.sleep(0.05)
            item['book_description'] = info.xpath('.//a[@class="sellPoint"]/@title').get()

        yield item
