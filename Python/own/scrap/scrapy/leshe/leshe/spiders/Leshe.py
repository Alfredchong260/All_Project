from ..items import LesheItem
from tqdm import tqdm
import scrapy
import time

class LesheSpider(scrapy.Spider):
    name = 'Leshe'
    allowed_domains = ['www.leshetu.top']
    start_urls = ['https://www.leshetu.top/xz/page/1']

    def parse_detail(self, response):
        item = LesheItem()
        img_lst = response.css('.container p noscript')
        for img in tqdm(img_lst):
            img_url = img.css('img').re('<img src="(.*?)">')[0]
            item['img_url'] = img_url
            yield item
        time.sleep(1)

    def secondRequest(self, response):
        div_lst = response.css('.col-lg-1-5.col-6.col-sm-6.col-md-4.col-lg-3')
        for div in div_lst:
            second_url = div.css('h2.entry-title a').re('<a target="_blank" href="(.*?)" title=".*?" rel="bookmark">.*?</a>')[0]
            
            yield scrapy.Request(url=second_url, callback=self.parse_detail)

        
    def parse(self, response):
        total_page = response.css('a.page-numbers::text').getall()[-1]
        for page in range(1, int(total_page) + 1):
            url = 'https://www.leshe.org/xz/page/{}'.format(page)

            yield scrapy.Request(url=url, callback=self.secondRequest)
