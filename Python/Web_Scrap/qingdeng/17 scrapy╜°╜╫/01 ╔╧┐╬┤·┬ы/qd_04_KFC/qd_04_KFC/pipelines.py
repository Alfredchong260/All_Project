# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class CsvPipeline(object):
    def __init__(self):
        self.f = open('KFC.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['storeName', 'addressDetail', 'pro'])
        self.csv_write.writeheader()  # 写入表头, 只写一次表头

    def process_item(self, item, spider):
        d = dict(item)
        self.csv_write.writerow(d)  # 一条一条的写入数据

        return item


    def close_spider(self, spider):
        self.f.close()  # # 项目停止前会关闭文件
