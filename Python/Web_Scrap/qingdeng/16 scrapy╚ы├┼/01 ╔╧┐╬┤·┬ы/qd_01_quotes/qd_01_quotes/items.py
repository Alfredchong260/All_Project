# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
scrapy项目定义的数据结构 {理解为字典} : 数据字段
    自定义
"""

class Qd01QuotesItem(scrapy.Item):  # 继承自此基类scrapy.Item
    # define the fields for your item here like:
    info = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

    """定义的字段名字最好和解析的字段变量名要一样, 避免后续出现错误"""