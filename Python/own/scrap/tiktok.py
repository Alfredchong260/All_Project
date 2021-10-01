from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import pickle
import random
import time
import os
import re


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'set-cookie': 'ttwid=1%7CWVaLmSyJoSYU3LgpnEbDK1-9FKXHbXZgUGQBTFkSlD0%7C1632206964%7C45638f214034d5ee9827a7e7a01d3081b336cecca5bfa9ca15a55a1bafed1699; Domain=.douyin.com; Path=/; Expires=Wed, 21 Sep 2022 08:20:29 GMT; HttpOnly'
}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']

proxy = {'HTTP': random.choice(proxies)}

base_url = 'https://www.douyin.com/?stay=1'

target_url = 'https://www.douyin.com/search/小姐姐'

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

class TikTok:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
        self.wait = WebDriverWait(self.driver, 10)
        self.status = 0
        self.login_method = 1

    def enter(self):
        while self.driver.title.find('抖音-记录美好生活') != -1:
            time.sleep(1)
        self.login()

    def set_cookies(self):
        # 登陆调用设置cookie
        self.driver.get(base_url)
        print('###请点击登陆###')
        # 如果没点击登陆，就会一直停留在首页，不会进行跳转
        while self.driver.title.find('抖音-记录美好生活') != -1:
            time.sleep(1)
        print('###请扫码###')

        pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb'))
        print('###cookie保存成功')
        self.driver.get(target_url)

    def get_cookie(self):
        cookies = pickle.load(open('./cookies.pkl', 'rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.douyin.com',
                'name': cookie.get('name'),
                'value': cookie.get('value')
            }
            self.driver.add_cookie(cookie_dict)
        print('###载入cookies###')

    def login(self):
        if self.login_method == 0:
            self.driver.get(base_url)
            self.driver.implicitly_wait(5)
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'login-guide__btn')))
            self.driver.find_element_by_class_name('login-guide__btn').click()
            print('###开始登陆###')
        elif self.login_method == 1:
            if not os.path.exists('./cookies.pkl'):
                self.get_cookie()
            else:
                self.driver.get(target_url)
                self.get_cookie()

    def getInfo(self, source):
        new_links = []
        links = re.findall(r'<a href="(https://www.douyin.com/video/\d+)" class=', source)
        for link in links:
            if link not in new_links:
                new_links.append(link)

        for i in new_links:
            print(i)


if __name__ == '__main__':
    test = TikTok()
    test.set_cookies()
