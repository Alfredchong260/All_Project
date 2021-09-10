import scrapy
from news.items import NewsItem


class SinchewSpider(scrapy.Spider):
    name = 'sinchew'
    allowed_domains = ['sinchew.com.my']
    start_urls = ['https://www.sinchew.com.my/']

    def parse(self, response):
        infos = response.css('.mp-smalltu-three')
        for info in infos:
            item = NewsItem()
            item['titles'] = info.xpath('./div/div[2]/a/text()').extract()
            item['links'] = info.xpath('./div/div[2]/a/@href').extract()
            item['date'] = info.css(".spinside-time ::text").extract()

            yield item 
