import scrapy
from tushu.items import TushuItem


class WangyiyunSpider(scrapy.Spider):
    name = 'wangyiyun'
    allowed_domains = ['yuedu.163.com']
    start_urls = ['https://yuedu.163.com/book/category']

    def parse(self, response):
        item = TushuItem()
        infos = response.xpath('//ul[@class="nav-list"]')
        titles = response.xpath('//div[@class="yd-book-content yd-book-content-standalone yd-store-content-container clearfix"]')
        a = []
        for info in infos:
            item['name'] = info.xpath('./li/div/a/text()').getall()
            links = info.xpath('./li/div/a/@href').getall()
            for i in links:
                link = 'https://yuedu.163.com' + i
                a.append(link)
            item['link'] = a

            for title in titles:
                item['title'] = title.xpath('./div/a/h2/text()').getall()
                item['artist'] = title.xpath('./div/div[1]/dl/dd/text()').getall()
                rates = title.xpath('./div/div[2]')
                rate = []

                for i in rates:
                    a = i.css('.no')
                    if len(a) == None:
                        rate.append(0)
                    rate.append(5 - len(a))

                item['rate'] = rate
                print(item)
                yield item


        start = response.xpath('//div[@class="m-page m-page-g"]')
        next = start.xpath('./a/@href').get()
        url = response.urljoin(next)
        for i in range(2, 101):
            a = url.replace('p2', "p{}".format(str(i)))
            yield scrapy.Request(url=a, callback=self.parse)


        yield scrapy.Request(url=url, callback=self.parse)
