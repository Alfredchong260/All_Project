# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class KfcPipeline:
    def process_item(self, item, spider):
        d = dict(item)
        with open('kfc.csv', 'w', encoding='utf-8') as fs:
            csv_writer = csv.writer(fs)
            csv_writer.writerow(f"{d[0]}, {d[1]}, {d[2]}")

        return item
