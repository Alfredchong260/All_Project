from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument('--proxy-server=211.144.27.126')

keyword = input('请输入商品关键字：')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

drive.get('https://www.jd.com/')
drive.implicitly_wait(10)

def get_product(keyword):
    '''实现商品搜索功能'''
    drive.find_element_by_css_selector('#key').send_keys(keyword)
    drive.find_element_by_css_selector('#key').send_keys(Keys.ENTER)
    sleep(1)

def scrollBotton():
    for i in range(1, 10, 2):
        drive.execute_script(f'window.scrollTo(0, document.body.scrollHeight*{i / 10})')
        sleep(1)

# 调用商品搜索功能
sleep(2)
get_product(keyword)
scrollBotton()

input()
drive.quit()
