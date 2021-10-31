import re
import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2. 执行浏览器自动化操作
"""常用方法"""
# get()  通过浏览器对象指定请求网址
driver.get('https://www.taobao.com/')

# save_screenshot()  截取浏览器页面的图片, 括号内部指定的是图片的名字
driver.save_screenshot('某宝.png')

"""
用selenium请求到数据以后, 做数据解析, 保证一定要以代码获取的数据为准
"""
# **重点**
# page_source  (属性)   查看页面渲染以后的数据(html)
# **因为用selenium和用浏览器在elements中看到的数据有可能有出入**
print(driver.page_source)  # 数据解析

# with open('a.html', mode='w', encoding='utf-8') as f:
#     f.write(driver.page_source)


# get_cookies() 查看请求以后的cookies
print(driver.get_cookies())

# current_url 查看当前请求的url地址
print(driver.current_url)

driver.maximize_window()  # 最大化浏览器

time.sleep(3)

driver.minimize_window()  # 最小化浏览器

input()
driver.quit()


'''
# import re
# re.findall('(.*?)', driver.page_source, re.S)


# driver.page_source 返回的就是html数据
selector = parsel.Selector(driver.page_source)
selector.xpath
selector.css
'''