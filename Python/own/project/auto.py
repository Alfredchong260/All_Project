import os
import time
import pickle
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

base_url = 'https://www.damai.cn/'

login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'

target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.352a5c61pC6ZR7&id=654388821537'

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

class Concert:
    def __init__(self) -> None:
        self.status = 0     # 状态，表示当前执行到哪个步骤
        self.login_method = 1 # {0:模拟登陆，1:cookie登录}
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

    def set_cookies(self):
        # 登陆调用设置cookie
        self.driver.get(base_url)
        print('###请点击登陆###')
        # 如果没点击登陆，就会一直停留在首页，不会进行跳转
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台') != -1:
            sleep(1)
        print('###请扫码###')

        while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座!':
            sleep(1)
        print('###扫码成功###')
        pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb'))
        print('###cookie保存成功')
        self.driver.get(target_url)

    # 假如本地有cookies.pkl,那么就直接获取
    def get_cookie(self):
        cookies = pickle.load(open('./cookies.pkl', 'rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.damai.cn',
                'name': cookie.get('name'),
                'value': cookie.get('value')
            }
            self.driver.add_cookie(cookie_dict)
        print('###载入cookies###')

    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
            print('###开始登陆###')
        elif self.login_method == 1:
            if not os.path.exists('./cookies.pkl'):
                self.get_cookie()
            else:
                self.driver.get(target_url)
                self.get_cookie()

    def enter_concert(self):
        '''打开浏览器'''
        print('###打开浏览器，进入大麦网###')
        self.login()            # 先进行登陆
        self.driver.refresh()   # 刷新页面
        self.status = 2
        print('登陆成功')

if __name__ == '__main__':
    test = Concert()
    test.set_cookies()
