# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titles = scrapy.Field()
    subs = scrapy.Field()
    links = scrapy.Field()
    book_name = scrapy.Field()
    book_img = scrapy.Field()
    book_description = scrapy.Field()
