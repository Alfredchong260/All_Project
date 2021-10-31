"""
目标网址: https://github.com/login 模拟登录

作业要求:
    1.用 selenium 模拟登录GitHub(首先自己注册一个账号)
温馨提示:
    这个网站加载速度很慢, 最好设置时间长一点的等待
请在下方编写代码
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

url = 'https://github.com/login'

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
drive.implicitly_wait(10)

drive.get(url)

# 查找用户名输入框
drive.find_element_by_id('login_field').send_keys('Alfredchong260@gmail.com')
time.sleep(1)

# 查找密码输入框
password = drive.find_element_by_id('password').send_keys('Chong6260')
time.sleep(1)

# 查找登陆按钮
drive.find_element_by_class_name('btn.btn-primary.btn-block.js-sign-in-button').click()

input()
drive.quit()
