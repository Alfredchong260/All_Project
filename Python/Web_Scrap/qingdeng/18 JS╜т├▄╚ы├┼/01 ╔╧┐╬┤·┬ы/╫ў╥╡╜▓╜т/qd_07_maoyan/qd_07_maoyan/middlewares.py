# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class Qd07MaoyanSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Qd07MaoyanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HeadersMiddleware:
    """headers中间件"""
    """
    'Cookie': '__mta=244152890.1603971211691.1618042413519.1618044198851.63; __mta=244152890.1603971211691.1618044198851.1634737108531.64; __mta=244152890.1603971211691.1618044198851.1637147494376.64; _lxsdk_cuid=1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8; __mta=244152890.1603971211691.1632809679672.1632897727972.102; uuid_n_v=v1; uuid=2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD; _lxsdk=2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD; _csrf=f567997d6fef6103a8e1f42bd215699d4a50553bd57aafac423d4afa490cdbbf; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1634733558,1636113288,1636381216,1637147494; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1637147494; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=17d2d984799-307-3f5-e00%7C%7C2',
    'Host': 'www.maoyan.com',
    'Referer': 'https://www.baidu.com/link?url=bQLDt5r-VYz3-_s57DWkzcE9l0uvWnGhQcsWKGgn2bUyNIloOwhp1q3mDLHxVgZV&wd=&eqid=8031b23500024ce2000000066194e362',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    """
    def process_request(self, request, spider):
        request.headers.update({
            # 'Cookie': '__mta=244152890.1603971211691.1618042413519.1618044198851.63; __mta=244152890.1603971211691.1618044198851.1634737108531.64; __mta=244152890.1603971211691.1618044198851.1637147494376.64; _lxsdk_cuid=1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8; __mta=244152890.1603971211691.1632809679672.1632897727972.102; uuid_n_v=v1; uuid=2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD; _lxsdk=2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD; _csrf=f567997d6fef6103a8e1f42bd215699d4a50553bd57aafac423d4afa490cdbbf; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1634733558,1636113288,1636381216,1637147494; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1637147494; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=17d2d984799-307-3f5-e00%7C%7C2',
            'Host': 'www.maoyan.com',
            'Referer': 'https://www.baidu.com/link?url=bQLDt5r-VYz3-_s57DWkzcE9l0uvWnGhQcsWKGgn2bUyNIloOwhp1q3mDLHxVgZV&wd=&eqid=8031b23500024ce2000000066194e362',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',

        })

        return None


class CookiesMiddleware:
    """cookies中间件"""
    """
    '__mta': '244152890.1603971211691.1618042413519.1618044198851.63',
    '__mta': '244152890.1603971211691.1618044198851.1634737108531.64',
    '__mta': '244152890.1603971211691.1618044198851.1637147494376.64',
    '_lxsdk_cuid': '1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8',
    '__mta': '244152890.1603971211691.1632809679672.1632897727972.102',
    'uuid_n_v': 'v1',
    'uuid': '2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD',
    '_lxsdk': '2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD',
    '_csrf': 'f567997d6fef6103a8e1f42bd215699d4a50553bd57aafac423d4afa490cdbbf',
    'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1634733558,1636113288,1636381216,1637147494',
    'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1637147494',
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    '_lxsdk_s': '17d2d984799-307-3f5-e00%7C%7C2',
    """
    def process_request(self, request, spider):
        request.cookies.update({
            '__mta': '244152890.1603971211691.1618042413519.1618044198851.63',
            '__mta': '244152890.1603971211691.1618044198851.1634737108531.64',
            '__mta': '244152890.1603971211691.1618044198851.1637147494376.64',
            '_lxsdk_cuid': '1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8',
            '__mta': '244152890.1603971211691.1632809679672.1632897727972.102',
            'uuid_n_v': 'v1',
            'uuid': '2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD',
            '_lxsdk': '2CA15B803E2F11EC89993550E45107B0ACB2725E5F644BB6BBA200295D260EFD',
            '_csrf': 'f567997d6fef6103a8e1f42bd215699d4a50553bd57aafac423d4afa490cdbbf',
            'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1634733558,1636113288,1636381216,1637147494',
            'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1637147494',
            '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
            '_lxsdk_s': '17d2d984799-307-3f5-e00%7C%7C2',
        })

        return None

