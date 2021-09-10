import scrapy
from ihuan.items import IhuanItem


class IpIhuanSpider(scrapy.Spider):
    name = 'ip.ihuan'
    allowed_domains = ['ip.ihuan.me']
    start_urls = ['http://ip.ihuan.me/']

    def parse(self, response):
        infos = response.xpath('//tbody/tr')
        item = IhuanItem()
        for info in infos:
            item['ips'] = info.xpath('./td[1]/a/text()').get()
            item['socks'] = info.xpath('./td[2]/text()').get()

            yield item

        next_page = response.xpath('//ul[@class="pagination"]/li[8]/a/@href').get()
        for i in range(5):
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)
