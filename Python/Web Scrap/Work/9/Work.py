import requests
from lxml import etree

url = 'https://bj.58.com/ershouche/'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Cookie": "id58=c5/nfGEbtUZ0PitnBQGVAg==; city=cs; 58home=cs; 58tj_uuid=6b99078b-a950-4c5e-af6a-6f9064905065; als=0; wmda_uuid=b1ebd23a695e0415cac36670669fb8ad; wmda_new_uuid=1; xxzl_deviceid=4cyINWwsYsK96SZ7Mf71HXF9%2FB4lCEuXdllHXAeqhiGZvniNf5hrPnBzwtbvJxM0; ppStore_fingerprint=4CABEF4E40DE44DC2BB1558C8A9A3867EA417C73C33DE447%EF%BC%BF1629212920612; new_uv=2; utm_source=; spm=; init_refer=; wmda_session_id_11187958619315=1629212922648-a7feeef2-a01d-1420; new_session=0; xxzl_cid=d259ffc1b7ab4261bf00c8301edd1530; xzuid=82f7fd99-de00-403e-bef2-b7d3cf5256e9; wmda_session_id_1409632296065=1629213487788-596d2b3d-9df6-362a; wmda_visited_projects=%3B11187958619315%3B1409632296065; gr_user_id=e6129a85-85fd-4bb7-bd3e-7009a2cdb6fb; gr_session_id_98e5a48d736e5e14=bd6eda58-c644-4522-ab94-d0e38acd519b; gr_session_id_98e5a48d736e5e14_bd6eda58-c644-4522-ab94-d0e38acd519b=true; sessionid=2f175fcd-2fa1-423b-bca2-c3fc1747aee5"
    }

class tongchen:
    def __init__(self, url):
        self.url = url

    # 获取所有内层链接
    def deep_url(self):
        li = []
        for i in range(1, 71):
            urls = url + "pn" + str(i) + "/"
            li.append(urls)
        self.urls = li

        return self.urls

    # 逐个内层连接都访问并提取需要的数据
    def all_response(self):
        urls = self.deep_url()
        all_links = []
        images = []
        types = []
        prices = []

        for url in urls:
            response = requests.get(url, headers=headers, proxies={'http': '59.55.162.4'}, timeout=5)
            html = etree.HTML(response.text)
            hyperlinks = html.xpath('//ul[@class="infos infos-card h-clearfix"]/li/div/a/@href')
            all_links.append(hyperlinks)

        # for url in urls:
        #     response = requests.get(url, headers=headers, proxies={'http': '117.94.222.176'}, timeout=5)
        #     html = etree.HTML(response.text)
        #     imgs = html.xpath('//ul[@class="infos infos-card h-clearfix"]/li/div/div[1]/@data-original')
        #     images.append(imgs)

        # for url in urls:
        #     response = requests.get(url, headers=headers, proxies={'http': '101.200.127.149'}, timeout=5)
        #     html = etree.HTML(response.text)
        #     type = html.xpath('//ul[@class="infos infos-card h-clearfix"]/li/div/div[2]/h2/span/text()')
        #     types.append(type)

        # for url in urls:
        #     response = requests.get(url, headers=headers, proxies={'http': '119.81.189.194'}, timeout=5)
        #     html = etree.HTML(response.text)
        #     price = html.xpath('//ul[@class="infos infos-card h-clearfix"]/li/div/div[3]/b/text()')
        #     prices.append(price)

        # return [all_links, images, prices]
        return all_links

    def visit_url(self, results):
        li = []
        for a in results:
            li.append(a)

        return li

if __name__ == "__main__":
    info = tongchen(url)
    print(info.all_response())
