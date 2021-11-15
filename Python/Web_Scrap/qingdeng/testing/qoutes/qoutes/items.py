# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QoutesItem(scrapy.Item): # 继承自此基类scrapy.Item
    # define the fields for your item here like:
    info = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
