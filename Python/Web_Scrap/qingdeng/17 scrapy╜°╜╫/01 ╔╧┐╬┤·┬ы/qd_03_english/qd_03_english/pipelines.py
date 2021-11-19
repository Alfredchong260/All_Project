# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import json

from itemadapter import ItemAdapter


# class Qd03EnglishPipeline:
#     def process_item(self, item, spider):  # item 每一条返回的数据结构是类字典对象
#         with open('english.csv', mode='a', encoding='utf-8', newline='') as f:
#             f.write(item['title'] + ',' + item['info'] + ',' + item['img_url'])
#             f.write('\n')
#         return item


class CsvPipeline(object):
    def __init__(self):
        """项目运行的初始化方法, 文件的打开, 连接数据库, 初始化方法在整个scrapy项目中只会调用一次"""
        self.f = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'info', 'img_url'])
        self.csv_write.writeheader()  # 写入表头, 只写一次表头

    # def open_spider(self, spider):
    #     """项目运行的初始化方法"""
    #     pass


    def process_item(self, item, spider):
        """
        process_item 处理item返回的每一条数据
        :param item:  爬虫返回的数据结构
        :param spider: 爬虫对象
        :return:  必须原路返回
        """

        d = dict(item)
        self.csv_write.writerow(d)  # 一条一条的写入数据

        return item  # return 必须得把item原路返回, 因为后续可能会有其他的管道需要这个 item 数据


    def close_spider(self, spider):
        """整个scrapy项目在停止之前的时候会自动调用的方法, 处理文件关闭..."""
        self.f.close()  # # 项目停止前会关闭文件


class JsonPipeline(object):
    def __init__(self):
        self.f = open('english.json', mode='w', encoding='utf-8')
        self.data_list = []  # 收集每一条 item 数据


    def process_item(self, item, spider):
        # item 是一个类字典对象
        d = dict(item)  # 转换成python原生的字典(坑)
        self.data_list.append(d)  # 把每一条数据添加到列表
        return item

    def close_spider(self, spider):
        """在scrapy项目停止前才会调用"""
        # json序列化
        json_data = json.dumps(self.data_list, ensure_ascii=False)
        # 写入json数据
        self.f.write(json_data)

        # 关闭json文件
        self.f.close()


"""
对接数据库
     def __init__(self):    建立数据库连接操作
     def process_item(self, item, spider):   执行数据写入
     def close_spider(self, spider):  关闭数据库连接操作
     
excel 
    
"""
