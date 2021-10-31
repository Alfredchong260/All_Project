import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.douban.com/')

# 首先点击读书
driver.find_element_by_css_selector('.anony-nav-links ul li:nth-child(1)').click()

# driver.window_handles  获取当前浏览器所有出窗口, 返回一个窗口对象的列表
# 可以根据窗口对象的列表索引切换窗口
print(driver.window_handles)

time.sleep(3)
driver.switch_to.window(driver.window_handles[0])


time.sleep(3)
driver.switch_to.window(driver.window_handles[1])

input()
driver.quit()

