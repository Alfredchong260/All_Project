import re
import os
import random
import requests
from tqdm import tqdm
from lxml import etree


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']

proxy = {'HTTP': random.choice(proxies)}

class crawler:
    def main(self):
        links = self.getTitle()
        links = links[1::]
        for link in links:
            self.firstRequest(link)

    def getTitle(self):
        url = 'https://www.5442tu.com/index.html'
        response = requests.get(url, headers=headers, proxies=proxy)
        html = etree.HTML(response.text)
        infos = html.xpath('//div[@class="nav both"]/ul/li')
        urls = []
        for info in infos:
            link = info.xpath('./a/@href')
            for i in link:
                urls.append(i)

        return urls

    def firstRequest(self, link):
        response = requests.get(link, headers=headers, proxies=proxy)
        html = etree.HTML(response.text)
        infos = html.xpath('//div[@class="imgList2"]/ul/li')
        urls = []
        for info in infos:
            link = info.xpath('./a/@href')
            urls.append(link[0])

        for url in urls:
            self.secondRequest(url)


    def secondRequest(self, url):
        response = requests.get(url, headers=headers, proxies=proxy)
        response.encoding = 'gb2312'
        html = etree.HTML(response.text)
        page = html.xpath('//div[@class="page"]/ul/li[1]/a/text()')
        for i in page:
            page = re.findall('共(\d)页:', i)
        urls = []
        next = url.split('.html')
        for num in range(2, int(page[0]) + 1):
            urls.append(url)
            url = next[0] + f'_{num}' + '.html'

        for url in tqdm(urls):
            self.downloadImg(url)

    def downloadImg(self, url):
        filename = './5442/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        response = requests.get(url, headers=headers, proxies=proxy)
        response.encoding = 'gb2312'
        html = etree.HTML(response.text)
        content = html.xpath('//div[@class="arcBody"]/p/a/@href')
        title = html.xpath('/html/head/title/text()')
        for i in content:
            response = requests.get(i, headers=headers, proxies=proxy).content
            with open(filename + title[0] + '.jpg', 'wb') as w:
                w.write(response)

if __name__ == '__main__':
    test = crawler()
    test.main()
