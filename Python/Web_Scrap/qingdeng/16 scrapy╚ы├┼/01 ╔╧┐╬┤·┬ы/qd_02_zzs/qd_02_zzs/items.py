# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd02ZzsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    info = scrapy.Field()
    reads = scrapy.Field()  # 阅读数
    commons = scrapy.Field()  # 点赞数
