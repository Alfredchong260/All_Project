# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
数据管道: 数据保存, 数据去重...
    在此项目中的所有数据都会流经数据管道
"""
class QuotesPipeline:

    def process_item(self, item, spider):
        # item 拿到爬虫数据结构返回的每一条数据
        d = dict(item)

        with open('quotes.csv', mode='a', encoding='utf-8') as f:
            f.write(d['info'] + ',' + d['author'] + ',' + '/'.join(d['tags']))
            f.write('\n')

        return item
