from tqdm import tqdm
import requests
import parsel
import time
import os

filename = './imgs/'

class LiangTu:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Host': 'i.hexuexiao.cn',
            'Referer': 'https://www.hexuexiao.cn/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        if not os.path.exists(filename):
            os.mkdir(filename)

    def FirstRequest(self):
        response = requests.get(url, self.headers)
        selector = parsel.Selector(response.text)
        divs = selector.css('.waterfall_warp')
        for div in divs:
            img_url = div.css('dd a::attr(href)').getall()
            titles = div.css('dd img::attr(title)').getall()
            for title in titles:
                self.CreateFile(title)
            yield img_url, titles

    def SecondRequest(self, url, title):
        response = requests.get(url, self.headers)
        selector = parsel.Selector(response.text)
        divs = selector.css('.swiper-wrapper')
        for div in divs:
            imgs = div.css('img::attr(src)').getall()
            index = 1
            for img in tqdm(imgs, desc=title):
                url = img.split('.300')[0]
                self.DownloadImg(url, index, title)
                time.sleep(1)
                index += 1

    def DownloadImg(self, url, index, title):
        response = requests.get(url)
        with open(filename + title + f'/{ index }.jpg', 'wb') as f:
            f.write(response.content)

    def run(self):
        data = self.FirstRequest()
        for i in data:
            for index, url in enumerate(i[0]):
                title = i[1][index]
                self.SecondRequest(url, title)

    def CreateFile(self, title):
        if not os.path.exists(filename + title):
            os.mkdir(filename + title)

url = 'https://www.hexuexiao.cn/meinv/rihanmeinv/'
test = LiangTu(url)
test.run()
