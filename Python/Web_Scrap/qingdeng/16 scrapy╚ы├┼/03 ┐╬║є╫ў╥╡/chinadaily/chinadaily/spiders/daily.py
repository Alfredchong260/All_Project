import scrapy
from ..items import ChinadailyItem


class DailySpider(scrapy.Spider):
    name = 'daily'
    allowed_domains = ['chinadaily.com']
    start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1, 11)]
    # START_URLS 只能发送GET请求

    def parse(self, response):
        div_list = response.css('.gy_box')
        for div in div_list:
            title = div.css('p.gy_box_txt2 a::text').get().strip()
            info = div.css('p.gy_box_txt3 a::text').get().strip()
            img_url = div.css('.gy_box_img img::attr(src)').get().strip()

            yield ChinadailyItem(title=title, info=info, img_url=img_url)
