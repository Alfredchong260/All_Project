import scrapy
from ..items import KfcItem


class KfcSpider(scrapy.Spider):
    name = 'kfc'
    allowed_domains = ['kfc.com.cn']
    # 查询参数 怎么传递 只能在请求地址直接些，scrapy框架不支持查询参数的构建
    # start_urls = ['http://www.kfc.com.cn/kfccoda.cn/ashx/GetStoreList.ashx?op=keyword']

    def start_requests(self):
        # scrapy.FormRequest() 是scrapy框架封装发送POST请求的方法
        yield scrapy.FormRequest(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                 formdata={
                                     'cname': '',
                                     'pid': '',
                                     'keyword': '北京',
                                     'pageIndex': '1',
                                     'pageSize': '10'
                                 },
                                 callback=self.parse,
                                 meta={'page': 2} # 用于scrapy框架函数与函数之间的数据传递
                                 )

    def parse(self, response):
        data = response.json()['Table1']

        for ls in data:
            storeName = ls['storeName']
            addressDetail = ls['addressDetail']
            pro = ls['pro']

            yield KfcItem(storeName=storeName, addressDetail=addressDetail, pro=pro)

        print(response.meta.get('page'))
        page = response.meta.get('page')

        if page <= 10:
            yield scrapy.FormRequest(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                     formdata={
                                         'cname': '',
                                         'pid': '',
                                         'keyword': '北京',
                                         'pageIndex': str(page),
                                         'pageSize': '10'
                                     },
                                     callback=self.parse,
                                     meta={'page': page + 1}
                                     )

        pass
