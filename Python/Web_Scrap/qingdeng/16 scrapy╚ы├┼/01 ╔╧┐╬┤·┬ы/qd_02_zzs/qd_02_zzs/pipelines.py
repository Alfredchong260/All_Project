# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Qd02ZzsPipeline:
    def process_item(self, item, spider):
        # item 拿到爬虫数据结构返回的每一条数据
        d = dict(item)

        with open('zzs.csv', mode='a', encoding='utf-8') as f:
            f.write(d['title'] + ',' + d['info'] + ',' + d['reads'] + ',' + d['commons'])
            f.write('\n')

        return item
