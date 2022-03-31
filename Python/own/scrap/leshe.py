import concurrent.futures
from tqdm import tqdm
import threading
import requests
import random
import time
import os
import re

lock = threading.Lock()

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
proxy = {'HTTP': random.choice(proxies)}

filename = './leshe/'
if not os.path.exists(filename):
    os.mkdir(filename)

obj = re.compile('.*?<h2 class="entry-title"><a target="_blank" href="(.*?)" title=".*?" rel="bookmark">.*?</a></h2>', re.S)

class Leshe:
    def __init__(self, url):
        self.url = url

    def initialize(self):
        response = requests.get(self.url, headers=headers, proxies=proxy)
        pages = re.findall('.*?<a class="page-numbers" href=".*?">(\d{1,3})</a>.*?', response.text, re.S)

        return pages[-1]

    def sendRequests(self):
        response = requests.get(self.url, headers=headers, proxies=proxy, timeout=3)
        links = re.findall(obj, response.text)

        return links

    def secondRequests(self, link):
        response = requests.get(link, headers=headers, timeout=3)
        title = re.findall('<h1 class="entry-title">(.*?)</h1>', response.text, re.S)
        link = re.findall('<img class="lazyload " src=".*?" data-srcset="(.*?)" title=".*?" alt=".*?" />', response.text, re.S)
        if not link:
            link = re.findall('<img.*?src="(.*?)".*?<br />', response.text, re.S)
        
        for i in tqdm(link):
            if i.startswith('http'):
                self.downloadImg(title, i)

    def downloadImg(self, title, url):
        if not os.path.exists(filename + title[0]):
            os.mkdir(filename + title[0])

        response = requests.get(url)
        name = url.split('/')[-1]

        lock.acquire()
        with open(filename + title[0] + '/' + name, 'wb') as w:
            w.write(response.content)
        lock.release()

        time.sleep(2)

    def run(self):
        links = self.sendRequests()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
            for link in links:
                exe.submit(self.secondRequests, link)

if __name__ == "__main__":
    url = input('请输入目标地址：')
    test = Leshe(url)
    pages = test.initialize()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as exe:
        for page in range(1, int(pages) + 1):
            new_url = f"{url}/page/{page}"
            main = Leshe(new_url)
            exe.submit(main.run)
