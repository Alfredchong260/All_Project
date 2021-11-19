# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class MaoyanPipeline:
    def __init__(self):
        self.fs = open('Maoyan.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.fs, fieldnames=['name', 'star', 'releasetime', 'score'])
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        d = dict(item)
        self.csv_write.writerow(d)

        return item


    def close_spider(self, spider):
        self.fs.close()
