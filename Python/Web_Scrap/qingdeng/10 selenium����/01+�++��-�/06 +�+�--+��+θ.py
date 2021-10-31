# 在百度搜索框输入  python ，全选,复制,剪切,粘贴 跳转到搜狗输入框进行搜索
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.baidu.com/')

input_label = driver.find_element_by_css_selector('#kw')
input_label.send_keys('python')
time.sleep(3)

input_label.send_keys(Keys.CONTROL, 'a')  # 全选
time.sleep(3)

input_label.send_keys(Keys.CONTROL, 'c')  # 复制
time.sleep(3)

input_label.send_keys(Keys.CONTROL, 'x')  # 剪切
time.sleep(3)

driver.get('https://www.sogou.com/')
driver.find_element_by_css_selector('#query').send_keys(Keys.CONTROL, 'v')  # 粘贴
time.sleep(3)

driver.find_element_by_css_selector('#query').send_keys(Keys.ENTER)
time.sleep(3)
input()
driver.quit()
"""
而且selenium所有的send_keys()方法都是基于元素操作的，没有元素无法操作。
"""