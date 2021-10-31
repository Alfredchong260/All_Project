from selenium.webdriver.chrome.options import Options  # 浏览器的可选项

from selenium import webdriver


chrome_options = Options()  # 实例化对象
chrome_options.add_argument('--headless')  # 添加一个可选项  # --headless 指代无头模式
# 创建浏览器对象的时候添加配置
driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)

driver.get('https://www.baidu.com/')

print(driver.page_source)

input()
driver.quit()

"""
    无头模式, 一般用于项目完成后添加
    无头模式对于一些浏览器的动作操作, 不支持
"""