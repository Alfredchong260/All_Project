# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class FulibaPipeline:
    def __init__(self) -> None:
        self.fs = open('fuliba.csv', 'a', encoding='utf-8')
        self.csv = csv.DictWriter(self.fs, fieldnames=['title', 'put_time', 'comments', 'starts', 'info'])
        self.csv.writeheader()

    def process_item(self, item, spider):
        d = dict(item)
        self.csv.writerow(d)

        return item

    def close_spider(self, spider):
        self.fs.close()
