'''
全局思路：
    到一个搜索引擎引用它的搜索功能
    输入搜索关键字
    在动态页面中获取照片的链接
    访问链接并得到内容
    将链接返回的内容以二进制写入.jpg文件
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os
import random
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

web = webdriver.Chrome('/usr/local/bin/chromedriver')
class DuckDuckGo:
        
    def main(self, url):
        
        self.mkdir()
        option = Options()
        option.add_argument('--disable-blink-features=AutomationControlled')
        web.get(url)
        sleep(1)
        a = web.find_elements_by_xpath('//div[@class="islrc"]/div/a[1]/div/img')
        all_a = []
        for i in a:
            link = i.get_property('src')
            all_a.append(link)
        num = 0
        all = []
        for a in all_a:
            all.append(a)
        print(all)
        sleep(1)
        logo = self.random_logo()
        for i in all:
            num += 1
            response = self.second_visit(link=i)

            if response == None or response == '':
                pass
            else:
                self.download_img(name=num, response=response, logo=logo)

    def second_visit(self, link):
        try:
            response = requests.get(link, headers=headers)
            return response.content
        except Exception:
            pass


    def download_img(self, name, response, logo):
        with open(f'./img/{logo}{name}.jpg', 'wb') as f:
            f.write(response)

    def mkdir(self):
        try:
            os.mkdir('img')
        except Exception:
            pass

    def random_logo(self):
        li = list('''!@#$%^&*()_+-={|};'",./<>?''')

        return random.choice(li)

if __name__ =='__main__':
    test = DuckDuckGo()
    while True:
        info = input('请输入你要查询的关键字眼：')
        if info.upper() == 'Q':
            break
        url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X".format(info)
        test.main(url)
