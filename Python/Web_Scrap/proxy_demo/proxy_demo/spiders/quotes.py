import scrapy
from proxy_demo.items import ProxyDemoItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # 获取class加.  获取id加#
        quotes = response.css('.quote')
        for quote in quotes:
            # extract_first() 代表之获取一个数据
            # extract() 代表获取多个数据
            item = ProxyDemoItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()

            yield item
            
            next = response.css('.next a::attr("href")').extract_first()
            url = response.urljoin(next)

        yield scrapy.Request(url=url, callback=self.parse)
