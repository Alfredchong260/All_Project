import scrapy

# scrapy.Spider  爬虫基类
class QuotesSpider(scrapy.Spider):
    # 爬虫文件的名字: 后续在运行项目的时候需要根据名字运行
    name = 'quotes'

    # 运行项目的时候, 请求采集的数据, 都会限制在该域名下, 限制的域名是一个列表, 后续可添加域名
    allowed_domains = ['toscrape.com']

    # 数据采集的起始网址, 一般需要修改起始网址, 因为是自动生成的
    # 是一个列表, 凡是列表里面的网址, 后续都会被请求
    # 如果采集的地址有规律, 一般会通过列表推导式, 推导所有地址
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # start_urls  网址中所有的地址, 默认都会给 parse 函数处理
        # parse 函数必须有 response 参数
        # response = 具有所有响应体方法及属性 + 具有之前所学的所有数据解析的方法<xpath css re>
        # print(response.text)

        """parse函数主要处理的就是数据的解析"""
        divs = response.css('.quote')  # 提取所有的 div 标签

        for div in divs:
            info = div.css('.text::text').get()  # 名言警句
            author = div.css('.author::text').get()  # 作者
            tags = div.css('.tags a::text').getall()  # 标签

            # print(info, author, tags)
            # 如果获取的数据, 返回的是一个字典吗呢么scrapy框架会自动处理
            # 在爬虫文件中 所有的数据返回必须全部用 yield
            # 一条一条的返回数据
            yield {
                'info': info,
                'author': author,
                'tags': tags,
            }

"""
如何解决反爬?
如何保存数据?
框架调用的顺序是什么?
"""
