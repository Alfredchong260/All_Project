import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.douban.com/')


"""
text
    属性, 可以提取标签包含的文本内容, 支持链式调用
    
    因为css/xpath语法不支持属性提取, 只能定位标签对象
"""
result = driver.find_element_by_css_selector('.app>a').text
# print(result)


"""
get_attribute()
    方法, 可以根据属性名获取其标签的属性值, 支持链式调用
"""
result2 = driver.find_element_by_css_selector('.app>a').get_attribute('href')
# print(result2)


"""标签对象的动作(输入/点击)"""
# 1. 得找到你要操作的标签对象
input_label = driver.find_element_by_css_selector('.inp input')
"""
send_keys('长津湖')
    如果标签对象具有输入功能, 可以向输入框中输入数据, 支持链式调用
"""
input_label.send_keys('长津湖')

# 1. 得找到你要操作的标签对象
click_label = driver.find_element_by_css_selector('.bn input')
"""
click()     执行标签的点击操作, 需要标签具有点击事件
"""
click_label.click()


input()
driver.quit()

