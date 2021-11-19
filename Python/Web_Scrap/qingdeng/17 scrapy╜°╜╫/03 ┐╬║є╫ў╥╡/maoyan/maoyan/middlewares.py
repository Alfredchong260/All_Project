# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MaoyanSpiderMiddleware:
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


class MaoyanDownloaderMiddleware:
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
    def process_request(self, request, spider):
        request.headers.update({
            'Host': 'www.maoyan.com',
            'Referer': 'https://www.maoyan.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        })

        return None

class CookiesMiddleware:
    def process_request(self, request, spider):
        request.cookies.update({
            '__mta': '150844937.1628600961648.1634352452634.1634352466863.112',
            '__mta': '150844937.1628600961648.1634352466863.1637027846282.113',
            '_lxsdk_cuid': '17b302e848dc8-055d4409b77c8f-3d740e5b-2f7600-17b302e848dc8',
            '__mta': '150844937.1628600961648.1634093805737.1634125470280.81',
            'uuid_n_v': 'v1',
            'uuid': '68DC68903D3C11EC82A35568394E37893690D033832342B580DD724AB1F9B057',
            '_lxsdk': '68DC68903D3C11EC82A35568394E37893690D033832342B580DD724AB1F9B057',
            '_csrf': 'ae154a87e4ef916945a2ec0b19cd7b1cb66029e5043050e50af154d2a1436a40',
            'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1636009026,1637026014',
            '__mta': '150844937.1628600961648.1634352466863.1637026367255.113',
            'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1637027845',
            '_lxsdk_s': '17d265aa9ac-05a-84b-cda%7C%7C21'
        })

        return None
