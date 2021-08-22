'''
selenium是一个自动化测试工具，利用驱动浏览器中执行特定的动作，获取页面源代码，做到可见即可爬健康
对于一些javascript动态渲染的页面来说，爬取方式非常有效
http://npm.taobao.org/mirrors/chromedriver/92.0.4515.107/ 下载驱动器
'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

web = webdriver.Chrome("/usr/local/bin/chromedriver")

# 访问1网页
# web.get('https://www.baidu.com/')
# wait = WebDriverWait(web, 1)

# 查找节点
# web.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# web.find_element_by_xpath('//*[@id="su"]').click()

# 等待至这个元素出来才开始提取源代码
# wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="2"]/div/h3/a')))

# 获取网页源代码
# print(web.page_source)

# 前进和后退
# web.get('https://www.baidu.com/')
# time.sleep(1)
# web.get('https://www.bilibili.com/')
# time.sleep(1)
# web.get('https://www.taobao.com/')
# time.sleep(1)
# web.get('https://www.17k.com/')
# time.sleep(1)
# # 后退
# web.back()
# web.back()
# web.back()
# # 前进
# web.forward()
# web.forward()

# 获取cookie
web.get('https://www.baidu.com/')
# print(web.get_cookies())
# print(web.get_window_size())

# 打开一个新的窗口
web.execute_script('window.open()')
web.execute_script('window.open()')
# print(web.window_handles)
web.switch_to_window(web.window_handles[2])
web.get('https:/www.taobao.com/')
time.sleep(2)
web.switch_to_window(web.window_handles[1])
web.get('https://www.bilibili.com/')





# web.get('https://www.baidu.com')

# web.find_element_by_id('kw').send_keys('58同城')
# web.find_element_by_xpath('//*[@id="su"]').click()
# web.find_element_by_xpath('//*[@id="1"]/div/h3/a[1]').click()
# time.sleep(15)

# web.get('https://passport.58.com/login/?path=https%3A%2F%2Fbj.58.com%2F&source=58-homepage-pc&PGTID=0d100000-0000-11df-2200-8ef3fefea393&ClickID=2')

# web.find_element_by_xpath('//*[@id="mask_body_item_username"]').send_keys('123456')
# web.find_element_by_xpath('//*[@id="mask_body_item_newpassword"]').send_keys('1234567890abcdefghi')
# web.find_element_by_xpath('//*[@id="mask_body_item_login"]').click()
# time.sleep(15)
