import time
from selenium import webdriver
from selenium.webdriver.support.select import Select  # 下拉框的功能


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.jq22.com/demo/shengshiliandong/')


# 找到有下拉框对应的 <select>
select = driver.find_element_by_css_selector('#s_province')

# 实例化下拉框对象
sel = Select(select)

"""选择下拉框"""
# 根据索引值取下拉框, 从1开始
sel.select_by_index(1)  # 北京市
time.sleep(3)

# 根据下拉框的 value 取值
sel.select_by_value('河北省')
time.sleep(3)

# 根据下拉框标签的文本取值
sel.select_by_visible_text('吉林省')
time.sleep(3)


input()
driver.quit()
