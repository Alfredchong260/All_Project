import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.douban.com/')

"""解析数据"""
# 根据标签的id属性值获取标签
result = driver.find_element_by_id('anony-sns')
# print(result)

# 根据标签的 name 属性值获取标签
result2 = driver.find_element_by_name('description')
# print(result2)

# 根据标签的 class 属性值获取标签
result3 = driver.find_elements_by_class_name('section')
# print(result3)

# 根据标签包含的文本内容获取到标签(精确匹配)
result4 = driver.find_element_by_link_text('下载豆瓣 App')
# print(result4)

# 根据标签包含的文本内容获取到标签(模糊匹配)
result5 = driver.find_elements_by_partial_link_text('豆瓣')
# print(result5)


print('+' * 100)

# 根据标签的名字获取标签
result6 = driver.find_elements_by_tag_name('div')
# print(result6)
# print(len(result6))


# 根据xpath获取标签, 支持二次提取
# 在selenium中, xpath语法不支持属性提取, 只能定位标签对象
result7 = driver.find_elements_by_xpath('//div[@class="anony-nav-links"]/ul/li')

# for li in result7:
#     li.find_element_by_xpath()
# print(result7)
# print(len(result7))


# 根据css获取标签, 支持二次提取
# 在selenium中, css语法不支持属性提取, 只能定位标签对象
result8 = driver.find_elements_by_css_selector('.anony-nav-links ul li')
print(result8)
print(len(result8))



# input()
driver.quit()

