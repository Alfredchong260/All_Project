import scrapy

from ..items import Qd04KfcItem


class KfcSpider(scrapy.Spider):
    name = 'KFC'
    allowed_domains = ['kfc.com.cn']
    # 查询参数? 怎么传递?  在请求地址中直接写, scrapy框架不支持查询参数的构建
    # start_urls = ['http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword']

    def start_requests(self):
        # scrapy.FormRequest()  是scrapy框架封装的发送 post 请求的方法
        yield scrapy.FormRequest(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                 formdata={
                                    'cname':'',
                                    'pid':'',
                                    'keyword': '北京',
                                    'pageIndex': '1',
                                    'pageSize': '10'
                                 },
                                 callback=self.parse,
                                 meta={'page': 2}  # 用于scrapy框架中函数与函数间的数据传递
                                 )

    def parse(self, response):
        # print(response.json())
        data_list = response.json()['Table1']

        for ls in data_list:
            storeName = ls['storeName']
            addressDetail = ls['addressDetail']
            pro = ls['pro']
            # print(storeName, addressDetail, pro)

            yield Qd04KfcItem(storeName=storeName, addressDetail=addressDetail, pro=pro)

        print('上个函数传下来的meta', response.meta.get('page'))

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
                                     meta={'page': page + 1}  # 基于上面函数传下来的 page 自增
                                     )

