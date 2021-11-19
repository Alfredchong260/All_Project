# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


"""
SpiderMiddleware: 爬虫中间件
    主要作用: 过滤错误请求<常见错误的状态码在scrapy底层会自动帮助你过滤>
    
DownloaderMiddleware:  下载中间件
    主要作用: 处理请求的伪装<headers  cookies  proxies>
    
"""

def get_proxy():
    """获取代理的函数"""
    proxy_json = requests.get(
        url='http://tiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=1&sb=&mr=2&sep=0&time=2').json()
    # print('获取到的代理:', proxy_json)
    proxy = proxy_json['data'][0]['ip'] + ":" + str(proxy_json['data'][0]['port'])
    # print('提取出来的代理:', proxy)

    """scrapy框架使用代理直接传   代理:端口"""
    # proxies = {
    #     "http": "http://" + proxy,
    #     "https": "http://" + proxy,
    # }
    return proxy



class HeadersMiddleware:
    """headers 中间件"""
    def process_request(self, request, spider):
        # request.headers 拿到的是一个请求体中的请求头, 是一个字典
        request.headers.update(
            {
                'Cookie': 'bid=nJ5mbBL3XUQ; __gads=ID=d4e33a95e1a5dad6-226538e329c600e1:T=1614424616:RT=1614424616:S=ALNI_MZ_Tj6BNEWUbp4D-BvvCiuahdGlNw; ll="118267"; __yadk_uid=RFh6Mvp3Q0kHQrj9HrxBbKJmG73HbVNK; gr_user_id=68d4d6d7-4109-4c05-9bfd-681a6915e8de; _vwo_uuid_v2=D4C3FBDACFA2E2318ADF6AC1B3BB844AE|4d0c5b80ba8c50e923415ca2315254f7; _ga=GA1.2.989597980.1611321780; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1636981716%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DYR3wwt31gOqxVjkIi_yNvkKTX2wZmfv8si7rKjnSI-4pkDlJ5RzN2K3a5NtwUfDx%26wd%3D%26eqid%3Def214a6a000181ea0000000661925bd2%22%5D; _pk_id.100001.4cf6=55c37287cf2a05f6.1611321773.28.1636981716.1636381516.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.989597980.1611321780.1636380896.1636981716.39; __utmb=30149280.0.10.1636981716; __utmc=30149280; __utmz=30149280.1636981716.39.29.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.834357791.1611321780.1636381428.1636981717.27; __utmb=223695111.0.10.1636981717; __utmc=223695111; __utmz=223695111.1636981717.27.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
                'Host': 'movie.douban.com',
                'Referer': 'https://www.baidu.com/link?url=YR3wwt31gOqxVjkIi_yNvkKTX2wZmfv8si7rKjnSI-4pkDlJ5RzN2K3a5NtwUfDx&wd=&eqid=ef214a6a000181ea0000000661925bd2',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            }
        )
        return None

class CookiesMiddleware:
    """Cookies 中间件"""
    def process_request(self, request, spider):
        # request.cookies 拿到的是一个请求体中的请求头, 是一个字典
        # 也可以把cookies的每一个片段构建成字典的每一个键值对
        cookies = {'Cookie': 'bid=nJ5mbBL3XUQ; __gads=ID=d4e33a95e1a5dad6-226538e329c600e1:T=1614424616:RT=1614424616:S=ALNI_MZ_Tj6BNEWUbp4D-BvvCiuahdGlNw; ll="118267"; __yadk_uid=RFh6Mvp3Q0kHQrj9HrxBbKJmG73HbVNK; gr_user_id=68d4d6d7-4109-4c05-9bfd-681a6915e8de; _vwo_uuid_v2=D4C3FBDACFA2E2318ADF6AC1B3BB844AE|4d0c5b80ba8c50e923415ca2315254f7; _ga=GA1.2.989597980.1611321780; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1636981716%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DYR3wwt31gOqxVjkIi_yNvkKTX2wZmfv8si7rKjnSI-4pkDlJ5RzN2K3a5NtwUfDx%26wd%3D%26eqid%3Def214a6a000181ea0000000661925bd2%22%5D; _pk_id.100001.4cf6=55c37287cf2a05f6.1611321773.28.1636981716.1636381516.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.989597980.1611321780.1636380896.1636981716.39; __utmb=30149280.0.10.1636981716; __utmc=30149280; __utmz=30149280.1636981716.39.29.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.834357791.1611321780.1636381428.1636981717.27; __utmb=223695111.0.10.1636981717; __utmc=223695111; __utmz=223695111.1636981717.27.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',}
        request.cookies.update(cookies)
        return None

class ProxyMiddleware:
    """Proxy 中间件"""
    def process_request(self, request, spider):
        # request.meta['proxy'] 针对请求设置代理
        request.meta['proxy'] = get_proxy()

        return None
    """有时候代理不可用"""
