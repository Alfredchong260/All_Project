import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.baidu.com/')
time.sleep(3)

driver.get('http://news.baidu.com/')
time.sleep(3)

driver.back()  # 返回到上一个页面
time.sleep(3)

driver.forward()  # 前进到下一个页面
time.sleep(3)

driver.refresh()  # 刷新页面

input()
driver.quit()
