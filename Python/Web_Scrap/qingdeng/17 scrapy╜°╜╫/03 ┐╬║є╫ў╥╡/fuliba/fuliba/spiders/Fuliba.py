from ..items import FulibaItem
import scrapy

class FulibaSpider(scrapy.Spider):
    name = 'Fuliba'
    allowed_domains = ['fuliba2021.net']
    start_urls = [f'https://fuliba2021.net/page/{page}' for page in range(1, 146)]

    def parse(self, response):
        article_lst = response.css('div.content article')
        for article in article_lst:
            title = article.css('header h2 a::text').get().strip()
            put_time = article.css('p.meta time::text').get().strip()
            comments = article.css('p.meta a::text').get()
            starts = article.css('p.meta a.post-like span::text').get()
            info = article.css('p.note::text').get().strip()

            yield FulibaItem(title=title, put_time=put_time, comments=comments, starts=starts, info=info)
