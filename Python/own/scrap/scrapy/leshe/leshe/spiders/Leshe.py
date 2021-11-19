import scrapy
from ..items import LesheItem


class LesheSpider(scrapy.Spider):
    name = 'Leshe'
    allowed_domains = ['leshe.org']
    start_urls = ['https://www.leshe.org/xz']

    def parse_detail(self, response):
        item = response.meta['item']
        img_lst = response.css('.container p noscript')
        for img in img_lst:
            img_url = img.css('img').re('<img src="(.*?)">')[0]
            item['img_url'] = img_url
            yield item
        
    def parse(self, response):
        item = LesheItem()
        div_lst = response.css('.col-lg-1-5.col-6.col-sm-6.col-md-4.col-lg-3')
        item = LesheItem()
        for div in div_lst:
            second_url = div.css('h2.entry-title a').re('<a target="_blank" href="(.*?)" title=".*?" rel="bookmark">.*?</a>')[0]
            # print(second_url)
            
            yield scrapy.Request(url=second_url, callback=self.parse_detail, meta={'item': item})
