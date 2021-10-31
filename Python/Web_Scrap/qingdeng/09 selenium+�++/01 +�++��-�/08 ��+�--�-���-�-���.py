import time

from selenium import webdriver

# 1. 创建一个浏览器对象
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2. 执行浏览器的自动化操作
driver.get('https://gitee.com/')
driver.implicitly_wait(10)  # 设置隐式等待
driver.maximize_window()  # 最大化浏览器

# undetected_chromedriver
"""浏览器的自动化, 和用户平常操作浏览器的顺序大致一样"""
# 找到登录按钮点击
driver.find_element_by_css_selector('.item.git-nav-user__login-item').click()

# 找到账号输入框, 输入账号
driver.find_element_by_css_selector('.login-password__account-input').send_keys('2535513449@qq.com')
time.sleep(2)

# 找到密码输入框, 输入密码
driver.find_element_by_css_selector('#user_password').send_keys('hjx_3136419')
time.sleep(2)

# 点击登录按钮
driver.find_element_by_name('commit').click()


input()
driver.quit()
