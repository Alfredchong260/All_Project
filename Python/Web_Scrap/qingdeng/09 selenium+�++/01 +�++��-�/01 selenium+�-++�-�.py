

# 导入浏览器模块
from selenium import webdriver


# 1. 创建一个浏览器对象
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2. 执行浏览器自动化操作
driver.get('https://www.baidu.com/')

# 3. 关闭浏览器
input()  # 阻止浏览器关闭 输入函数
driver.close()  # 关闭当前页面
driver.quit()  # 退出整个浏览器


