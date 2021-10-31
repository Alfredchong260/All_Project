import time

from selenium import webdriver
from selenium.webdriver import ActionChains  # 导入鼠标动作链的功能


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

driver.switch_to.frame(0)
drag = driver.find_element_by_css_selector('#draggable')
drop = driver.find_element_by_css_selector('#droppable')

action = ActionChains(driver)
action.drag_and_drop(drag, drop)
action.perform()

"""处理弹窗"""
alert = driver.switch_to_alert()  # 切换到弹窗
print(alert.text)
time.sleep(2)
alert.accept() # 点击弹窗的确认

input()
driver.quit() # 退出