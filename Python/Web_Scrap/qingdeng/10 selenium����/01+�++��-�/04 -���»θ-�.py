from selenium import webdriver
from selenium.webdriver import ActionChains  # 导入鼠标动作链的功能


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 进入嵌套网页
driver.switch_to.frame(0)
# 找到可以拖动标签
drag = driver.find_element_by_css_selector('#draggable')
# 找到放置的位置
drop = driver.find_element_by_css_selector('#droppable')

"""鼠标动作链实现"""
# 1. 创建一个动作链对象, 传入浏览器的对象
action = ActionChains(driver)

# 2. 定义一个动作, 此动作到目前还没有被执行
action.drag_and_drop(drag, drop)

# 3. 执行动作链  perform()
action.perform()


input()
driver.quit() # 退出