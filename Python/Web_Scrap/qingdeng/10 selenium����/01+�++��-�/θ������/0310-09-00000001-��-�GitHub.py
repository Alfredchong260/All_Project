"""
目标网址: https://github.com/login 模拟登录

作业要求:
    1.用 selenium 模拟登录GitHub(首先自己注册一个账号)
温馨提示:
    这个网站加载速度很慢, 最好设置时间长一点的等待
请在下方编写代码
"""
import csv
import time

from selenium import webdriver


# 1. 创建一个浏览器对象
driver = webdriver.Chrome(executable_path='chromedriver.exe')


# 2. 执行自动化操作
driver.get('https://github.com/login')
driver.maximize_window()
driver.implicitly_wait(10)

"""模拟登录"""
driver.find_element_by_css_selector('#login_field').send_keys('hjx-edu')
time.sleep(3)

driver.find_element_by_css_selector('#password').send_keys('qingdeng123')
time.sleep(3)

driver.find_element_by_css_selector('.btn.btn-primary.btn-block.js-sign-in-button').click()

# 3. 退出浏览器
input()  # 阻塞
driver.quit()


