import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.douban.com/')

time.sleep(3)

# js滚动页面的代码
# document.documentElement.scrollTop 指定页面滚动条的位置
# document.documentElement.scrollHeight   获取当前页面最大高度的代码
js = "document.documentElement.scrollTop=1000"
driver.execute_script(js)
# js = "document.documentElement.scrollTop=document.documentElement.scrollHeight"
time.sleep(3)

js2 = "document.documentElement.scrollTop=100"
driver.execute_script(js)
# execute_script() 执行js代码的方法, 括号内部传递js代码



input()
driver.quit() # 退出