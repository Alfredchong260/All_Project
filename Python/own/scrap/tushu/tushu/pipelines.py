# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class TushuPipeline:
    def __init__(self):
        self.file = open('WangYiYun.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')

    def open_spider(self, spider):
        self.exporter.start_exporting()
        print('爬虫开始')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print('爬虫结束')
