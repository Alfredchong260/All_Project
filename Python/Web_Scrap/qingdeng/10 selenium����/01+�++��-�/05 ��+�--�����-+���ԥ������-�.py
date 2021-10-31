import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://gitee.com/')
driver.implicitly_wait(10)  # 设置隐式等待
driver.maximize_window()  # 最大化浏览器
driver.find_element_by_css_selector('.item.git-nav-user__login-item').click()
driver.find_element_by_css_selector('.login-password__account-input').send_keys('2535513449@qq.com')
time.sleep(2)
driver.find_element_by_css_selector('#user_password').send_keys('hjx_3136419')
time.sleep(2)
driver.find_element_by_name('commit').click()

time.sleep(2)  # 消息提示弹出, 必须加强制等待
"""登录后解决消息提示<弹出(耗时)>"""
# context_click()  上下文点击 可以确定点击的坐标大概位置
# ActionChains(driver).move_by_offset(1073, 661).context_click().perform()
ActionChains(driver).move_by_offset(1073, 661).click().perform()



input()
driver.quit()
