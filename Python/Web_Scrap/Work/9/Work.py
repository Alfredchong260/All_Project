import requests
from lxml import etree
import random

'''
    全局思路：
        正常访问网页并提取数据
        二次访问到内层链接并从而提取数据
        将需要的数据整合成txt文件
    问题：
        1. 很常被封ip
    解决方法：
        1. 爬取实事ip地址并以这些ip地址进行访问(访问速度及其慢)
'''
url = 'https://bj.58.com/ershouche/'

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    # "Cookie": "id58=c5/nfGEb1KM9H2HcBsL2Ag==; city=bj; wmda_uuid=08e7e65a70710e0b055edc0ed62bbc55; wmda_new_uuid=1; wmda_visited_projects=%3B1409632296065%3B11187958619315%3B1732038237441; 58tj_uuid=7fde6170-3020-4aa5-a115-e975dd8e5c6e; new_uv=8; gr_user_id=1fa9055e-52cc-4696-8825-e6c63a22deaf; als=0; 58home=bj; xxzl_deviceid=1nDTSJOd1gPx4zw%2BqK0dlmHmMAMsxUcrCig2CKR6NbcBvMEcrcavcUvP3qdO9MxP; fzq_h=15909693b9a6cfd6aae98e9e32f7c0e0_1629364557433_9123f1dddf064213bc0542b07a973b8f_247518312; xxzl_token='Dwb8Jbu3lp/LoysInXW2GW…8Nin35brBb//eSODvMgkQULA=='; xxzl_sid='8I1PQT-PYt-LJu-TcQ-28Mi5MHqV'; sessionid=a3cf3c97-86c2-43f8-a231-7b3ad127b3a5; ppStore_fingerprint=00BAB037C561BDC8E97BF349911B52076F19E03F7AAB9A09%EF%BC%BF1629339193336; new_session=0; utm_source=; spm=; init_refer=https%253A%252F%252Fcallback.58.com%252F; wmda_session_id_11187958619315=1629368745273-23f3da6a-04ae-d7f8; xxzl_cid=c2c325b23fce47db9e3ebdd6bd0219ef; xzuid=985b476e-6fd6-48e8-aa4c-a99e1fd9fa07; wmda_session_id_1732038237441=1629369476360-07e82a65-ec0e-d6b8", 
    # "Referer":"https://bj.58.com/"
    }

class tongchen:
    def __init__(self, url):
        self.url = url

    # 得到多个网页的网页地址
    def get_multiple_url(self):
        url = 'https://www.kuaidaili.com/free/inha/'
        li = []
        for i in range(1, 10):
            url_ = url + str(i)
            li.append(url_)

        return li

    # 爬取网页上的ip地址
    def get_ip_list(self):
        li = []
        urls = self.get_multiple_url()
        for url in urls:
            r = requests.get(url, headers, proxies={"http": "161.202.226.194:80"})
            html = etree.HTML(r.text)
            ip = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[1]/text()')
            port = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[2]/text()')

            for i in range(0, len(ip)):
                ip_ = ip[i]
                port_ = port[i]
                li.append(ip_ + ":" + port_)
        return li

    # 检测ip地址是否能够正常访问
    def check_ip(self):
        valid = []
        ip_list = self.get_ip_list()
        for ip in ip_list:
            proxy_ip = "http://" + ip
            proxies = {'http': proxy_ip}
            try:
                response = requests.get(url='https://www.shopee.com/index.html', headers=headers, proxies=proxies, timeout=10)
                if response.status_code == 200:
                    return proxies
            except Exception:
                continue

        return valid

    # 设置所有要访问的页面
    def all_url(self):
        li = []
        for i in range(1, 71):
            urls = url + "pn" + str(i) + "/"
            li.append(urls)

        return li

    # 获得车辆的款式
    def get_title(self):
        types = []
        urls = self.all_url()
        for url in urls:
            response = requests.get(url, headers=headers, proxies=self.check_ip(), timeout=10)
            html = etree.HTML(response.text)
            type = html.xpath('//ul[@class="infos infos-card h-clearfix"]/li/div/a/div[2]/h2/span/@title')
            types.append(type)

        return types

    # 得到车辆的价格
    def get_prices(self):
        prices = []
        urls = self.all_url()
        for url in urls:
            response = requests.get(url, headers=headers, proxies=self.check_ip(), timeout=10)
            html = etree.HTML(response.text)
            price = html.xpath('//ul[@class="infos infos-card h-clearfix"]/li/div/a/div[3]/b/text()')
            prices.append(price)
        
        return prices

    # 设置格式
    def format(self, title, price):
        format = "车辆款式：{}\n车辆价格：\n\n".format(title, price)

        return format

    # 整合所得到的数据
    def get_data(self):
        title = self.get_title()
        price = self.get_prices()
        for i, j in zip(title, price):
            info = self.format(title=i, price=j)
            print(info)

if __name__ == "__main__":
    info = tongchen(url)
    print(info.get_title())

