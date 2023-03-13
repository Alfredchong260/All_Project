# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class HeadersMiddleware:
    def process_request(self, request, spider):
        # request.headers 拿到的是一个请求体中的请求头, 是一个字典
        request.headers.update(
            {'referer': 'https://www.leshe.org/xz',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            )

        return None
