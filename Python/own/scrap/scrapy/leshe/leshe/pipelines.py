# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter
import scrapy


class DownLoadPicture(ImagesPipeline):   # ImagesPipeline 专门请求二进制数据

    """保存二进制的管道类"""
    def get_media_requests(self, item, info):
        # item 能够拿到 item 返回的数据
        img_url = item['img_url']  # 图片地址
        yield scrapy.Request(url=img_url)

"""scrapy专题课程中会有图片名字的指定"""
