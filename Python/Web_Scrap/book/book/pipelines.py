# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter



class BookPipeline:
    def __init__(self):
	    self.file = open('tongcheng_pipeline.json', 'wb')
	    self.exporter = JsonItemExporter(self.file, encoding='utf-8')

    def open_spider(self, spider):
		#可选实现，当spider被开启时，这个方法被调用。
		#输出到tongcheng_pipeline.json文件
	    self.exporter.start_exporting()
        # print('爬虫开始')

    def process_item(self, item, spider):
	    self.exporter.export_item(item)
	    return item

    def close_spier(self, spider):
		#可选实现，当spider被关闭时，这个方法被调用
	    self.exporter.finish_exporting()
	    self.file.close()
        # print('爬虫结束!')
