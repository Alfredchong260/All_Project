from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('tanzhouketang@gmail.com')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('tanzhouketang123456')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(2)

driver.execute_script('window.open()')
driver.execute_script('window.open()')
time.sleep(2)

driver.switch_to_window(driver.window_handles[2])
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_id('su').click()
time.sleep(2)

driver.switch_to_window(driver.window_handles[1])
driver.get("https://www.bilibili.com")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys("罪恶王冠")
time.sleep(2)
driver.find_element_by_class_name("nav-search-btn").click()
time.sleep(2)

driver.switch_to_window(driver.window_handles[2])
driver.find_element_by_xpath('//*[@id="1"]/div/h3/a').click()
time.sleep(2)

driver.switch_to_window(driver.window_handles[2])
driver.execute_script('window.close()')
time.sleep(2)

driver.switch_to_window(driver.window_handles[2])
driver.execute_script('window.close()')
time.sleep(2)

driver.switch_to_window(driver.window_handles[2])
driver.find_element_by_id('id-search-field').send_keys('download')
driver.find_element_by_name('submit').click()
time.sleep(2)
driver.back()
time.sleep(5)
