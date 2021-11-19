# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv

# class ChinadailyPipeline:
#     def process_item(self, item, spider):

#         d = dict(item)

#         with open('chinadaily.csv', 'a', encoding='utf-8') as w:
#             w.write(f"{d['title']}, {d['info']}, {d['img_url']}")
#             w.write('\n')

#         return item

class CsvPipeline:
    def __init__(self):
        '''项目初始化方法，文件的打开，连接数据库，初始化方法在整个scrapy项目中只会调用一次'''
        self.fs = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv = csv.DictWriter(self.fs, fieldnames=['title', 'info', 'img_url'])
        self.csv.writeheader()  # 写入标头

    # def open_spider(self, spider):
    #     '''项目初始化方法，文件的打开，连接数据库'''
    #     pass

    def process_item(self, item, spider):
        """
        :param item: 处理item返回的每一条数据
        :param spider: 爬虫对象
        :return: item 必须原路返回
        """

        d = dict(item)
        self.csv.writerow(d)    # 一条一条的写入数据

        return item # return 必须把item原路返回，因为后续可能会有其他的管道需要这个item数据

    def close_spider(self, spider):
        """整个scrapy项目停止之前会自动调用的方法，处理文件关闭"""
        self.fs.close() # 项目停止前会关闭文件

        pass

class JsonPipeline:
    def __init__(self):
        self.fs = open('english.json', mode='w', encoding='utf-8')
        self.data_list = [] # 手机每一条item数据

    # def open_spider(self, spider):
    #     '''项目初始化方法，文件的打开，连接数据库'''
    #     pass

    def process_item(self, item, spider):
        # item 是个类字典对象
        d = dict(item)
        self.data_list.append(d) # 把每一条数据添加到列表

        return item

    def close_spider(self, spider):
        """在scrapy项目停止前才会调用"""
        # 写入json序列化数据
        self.fs.write(json.dumps(self.data_list, ensure_ascii=False))

        self.fs.close()

'''
对接数据库
    def __init__(self): 建立数据库连接操作
    def process_item(self, item, spider):
    def close_spider(self, spider):

excel
'''
