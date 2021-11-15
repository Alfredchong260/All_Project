# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ChinadailyPipeline:
    def process_item(self, item, spider):

        d = dict(item)

        with open('chinadaily.csv', 'a', encoding='utf-8') as w:
            w.write(f"{d['title']}, {d['info']}, {d['img_url']}")
            w.write('\n')

        return item
