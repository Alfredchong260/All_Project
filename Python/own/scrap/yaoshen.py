import random
import requests
import parsel
import os
import re
from tqdm import tqdm

headers = {
    'Referer':'https://www.kuimh.com/book/mh10575',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']

proxy = {'HTTP': random.choice(proxies)}

class yaoshenji:
    def main(self):
        url = 'https://www.kuimh.com/chapter/332265-3351141'
        response = requests.get(url, headers=headers, proxies=proxy)
        selector = parsel.Selector(response.text)
        urls = self.firstRequest(selector)

        global filename
        filename = './妖神记/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        print('正在读取并下载所有数据')
        for url in tqdm(urls):
            all = list(self.getInfos(url))
            links = all[0]
            name = all[1]

            name = name[0].split(' ')[1]

            for link in links[1::]:
                title = re.findall('http://img.aiquanjian.com/book/\d+/\d+/(.*?).jpg', link)
                self.downloadImages(url=link, title=title, file=name)

    def firstRequest(self, selector):
        chapters = []
        all_chapeters = selector.css('.mCustomScrollBox ul li a::attr(href)').getall()
        for i in all_chapeters:
            chapters.append('https://www.kuimh.com' + i)

        return chapters

    def getInfos(self, url):
        response = requests.get(url, headers=headers, proxies=proxy)
        selector = parsel.Selector(response.text)
        links = []
        names = []
        titles = selector.css('.row h1::text').get()
        names.append(titles)
        imgs = selector.css('.comicpage div img::attr(src)').getall()
        for i in imgs:
            if i.endswith('jpg'):
                links.append(i)
            else:
                new = selector.css('.comicpage div img::attr(data-echo)').getall()
                for i in new:
                    links.append(i)
                break

        return [links, names]

    def downloadImages(self, url, title, file):
        response = requests.get(url, headers=headers, proxies=proxy)
        file = file[0]
        if not os.path.exists(filename + file):
            os.mkdir(filename + file)
        with open(f"{filename}/{file}/{title}.jpg", 'wb') as w:
            w.write(response.content)

if __name__ == '__main__':
    test = yaoshenji()
    test.main()
