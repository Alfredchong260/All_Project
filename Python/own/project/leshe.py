from tqdm import tqdm
import requests
import parsel
import os
import re


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'cookie': 'ga=GA1.2.359235668.1631173779; _gid=GA1.2.2040819696.1631173779; Hm_lvt_56ff2ff29805a0d6ca5a4573276ffae7=1631173780,1631175228; PHPSESSID=1ce292mmmhdgcv15k1r4sunu7u; Hm_lpvt_56ff2ff29805a0d6ca5a4573276ffae7=1631175510'
}

class leshe:
    def __init__(self, url):
        self.url = url

    def main(self):
        filename = './lengluii'
        if not os.path.exists(filename):
            os.mkdir(filename)

        pages = self.initialize()
        self.startDownload(filename, pages)

    def initialize(self):
        sum = []
        response = requests.get(self.url, headers=headers)
        selector = parsel.Selector(response.text)
        page = str(selector.xpath('//ul[@class="page-numbers"]/li').getall())
        a = page.split(',')
        for i in a:
            try:
                obj = re.compile('<li><a class="page-numbers" href="(.*?)">(\d+)</a></li>')
                pages = obj.search(i).group(2)
                sum.append(pages)
            except Exception:
                pass

        return sum[-1]

    def startDownload(self, filename, pages):
        for page in range(1, int(pages)):
            url = self.url + f'page/{page}'
            response = requests.get(url, headers=headers)
            html = parsel.Selector(response.text)
            infos = html.xpath('//div[@class="row posts-wrapper"]/div')

            for info in tqdm(infos):
                titles = info.xpath('.//h2[@class="entry-title"]/a/text()').get()
                links = info.xpath('.//h2[@class="entry-title"]/a/@href').get()

                response1 = requests.get(url=links, headers=headers)
                selector = parsel.Selector(response1.text)
                img_url = selector.xpath('//p/img/@data-srcset').getall()

                if not os.path.exists(f'./{filename}/{titles}'):
                    os.mkdir(f'./{filename}/{titles}')

                for img in img_url:
                    name = img.split('/')[-1]
                    img_data = requests.get(url=img, headers=headers)
                    with open(f'./{filename}/{titles}/{name}', 'wb') as w:
                        w.write(img_data.content)

if __name__ == '__main__':
    url = input('请输入你要查找的乐摄网址：')
    test = leshe(url)
    test.main()
