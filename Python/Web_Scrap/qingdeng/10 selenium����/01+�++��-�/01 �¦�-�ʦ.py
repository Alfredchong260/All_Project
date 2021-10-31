from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://music.163.com/#/song?id=1450083773')


"""通过代码进入嵌套网页"""
"""第一种进入嵌套网页形式"""
# frame(0) 根据索引进入到嵌套网页, 索引值是从0开始的
# 索引值不能超出当前网页已有的嵌套数量
# driver.switch_to.frame(0)


"""第二种进入嵌套网页形式"""
# <iframe> 标签一般是嵌套网页标签
# 根据嵌套网页的<iframe>标签进入到嵌套网页
iframe = driver.find_element_by_css_selector('#g_iframe')
driver.switch_to.frame(iframe)  # 进入嵌套网页

driver.switch_to.parent_frame()  # 从当前嵌套网页, 切换回父网页

print(driver.page_source)

"""嵌套网页进入与退出, 最好一级一级去做"""

input()
driver.quit() # 退出

