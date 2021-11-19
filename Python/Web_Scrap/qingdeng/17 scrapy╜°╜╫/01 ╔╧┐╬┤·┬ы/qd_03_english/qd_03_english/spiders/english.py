import scrapy

from ..items import Qd03EnglishItem


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = []  # 列表<对采集的域名做限制>, 如果是空列表, 所有域名下的数据都可以采集
    # 构建地址翻页
    # start_urls 只能发送get请求
    # start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1, 11)]
    start_urls = ['https://language.chinadaily.com.cn/thelatest/']

    def parse(self, response):
        divs = response.css('.gy_box')

        for div in divs:
            title = div.css('.gy_box_txt2 a::text').get().strip()
            info = div.css('.gy_box_txt3 a::text').get().strip()
            img_url = div.css('.gy_box_img img::attr(src)').get().strip()

            # yield {'title':title,
            #         'info':info,
            #         'img_url':img_url
            #        }

            yield Qd03EnglishItem(title=title, info=info, img_url=img_url)

        # next_page = response.css('.next .pagestyle::attr(href)').get()
        #
        # page_num = int(response.css('.next .pagestyle::attr(href)').re('\d+')[0])
        #
        # if page_num <= 10:  # 判断翻页的页数
        #     all_url = 'https:' + next_page
        #     yield scrapy.Request(url=all_url, callback=self.parse)

