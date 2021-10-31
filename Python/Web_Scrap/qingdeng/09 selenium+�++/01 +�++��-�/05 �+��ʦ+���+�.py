import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.jd.com/')


"""强制等待, 死等"""
# time.sleep(5)  # 动态页面<弹出标签元素, 弹出验证码>

"""隐式等待"""
# 智能化等待
# 打开很多页面, 只需要设置一次隐式等待, 后续的页面都会遵循隐式等待的规则
# 如果超过了隐式等待的时间, 任然会报错
driver.implicitly_wait(5)


input()
driver.quit()

