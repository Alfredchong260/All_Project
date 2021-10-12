from tqdm import tqdm
import threading
import requests
import random
import time
import sys
import os
import re

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'cookie': 'ga=GA1.2.359235668.1631173779; _gid=GA1.2.2040819696.1631173779; Hm_lvt_56ff2ff29805a0d6ca5a4573276ffae7=1631173780,1631175228; PHPSESSID=1ce292mmmhdgcv15k1r4sunu7u; Hm_lpvt_56ff2ff29805a0d6ca5a4573276ffae7=1631175510'
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
proxy = {'HTTP': random.choice(proxies)}

filename = './lenglui/'

class leshe:
    def __init__(self, url):
        """实现得到要访问的网页"""
        self.url = url

    def main(self):
        """主函数，只要调用这个函数，其他函数就会环环相扣"""
        if not os.path.exists(filename):
            print(f'正在创建{filename}文件夹')
            os.mkdir(filename)

        response = requests.get(self.url, headers=headers).text
        num = self.number(response)
        print('开始扫描总页数')
        print(f'总页数为：{num}')

        for page in tqdm(range(1, int(num) + 1)):
            time.sleep(1)
            try:
                part = self.url.split('leshe.us/')[-1].split('/page/')[0]
            except Exception:
                part = self.url.split('leshe.us/')[-1]

            url = f"https://www.leshe.us/{part}/page/{page}"
            response = requests.get(url, headers=headers)
            firstRequests = threading.Thread(target=self.firstRequests, args=(response,))
            firstRequests.start()
    
    def number(self, response):
        """
        得到网页的总页数，并依次爬取
        :param response:首次访问网页返回的响应
        """
        obj = re.compile('<a class="page-numbers" href=".*?">(\d{1,4})</a>', re.S)
        num = re.findall(obj, response)

        return num[-1]

    def firstRequests(self, response):
        """
        第一次访问页面
        :param resposne:访问页面返回的响应
        """
        obj = re.compile('<a target="_blank" href="(.*?)".*?rel="bookmark">(.*?)</a>', re.S)
        data = re.findall(obj, response.text)
        try:
            for url, title in data:
                time.sleep(1)
                title = self.formatTitle(title)
                secondRequest = threading.Thread(target=self.secondRequest, args=(url, title))
                secondRequest.start()
        except requests.exceptions.ConnectionError:
            response.status_code = "Connection refused"

    def secondRequest(self, url, title):
        """
        二次访问网页，目的为得到需要的图片网址
        :param url:访问页面得到的网址，用于二次访问
        :param title:访问页面得到的标题，用于后面创建文件夹使用
        """
        response = requests.get(url, headers=headers)
        obj = re.compile('<img class="lazyload " src=".*?" data-srcset="(.*?)".*?</noscript>')
        img = re.findall(obj, response.text)
        for url in img:
            time.sleep(1)
            name = url.split('/')[-1]
            if not os.path.exists(f"{filename}{title}"):
                os.mkdir(f"{filename}{title}")
            downloadImage = threading.Thread(target=self.downloadImage, args=(url, title, name))
            downloadImage.start()

    def formatTitle(self, title):
        """
        格式化某些敏感符号，避免创建文件夹时出错
        :param title:需要格式化的标题，返回一个新的标题
        """
        new = re.sub('[.*?<>:/\|]', '', title)

        return new

    def downloadImage(self, url, title, name):
        """
        下载图片的函数
        :param url:需要下载的图片网址
        :param title:以格式化的标题，用于创建文件夹
        """
        response = requests.get(url, headers=headers)
        time.sleep(1)
        with open(f"{filename}{title}/{name}", 'wb') as w:
            w.write(response.content)

if __name__ == '__main__':
    # url = input('请输入你要查找的乐摄网址：')
    if sys.argv:
        try:
            response = requests.get(url=sys.argv[1], headers=headers)
        except:
            print('Invalid url')
            sys.exit()
    else:
        print('python3 leshe.py <url>')

    test = leshe(sys.argv[1])
    test.main()
    print('任务完成')

