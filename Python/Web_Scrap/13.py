# import csv

# 逗号分隔符文件

# 按行写入
# with open('data.csv', 'w') as w:
#     write = csv.writer(w, delimiter=' ')
#     write.writerow(['id', 'name', 'age'])
#     write.writerow(['1', 'mike', '20'])
#     write.writerow(['2', 'jack', '23'])
#     write.writerow(['3', 'bob', '21'])

# 同时写入多行
# with open('data.csv', 'w') as w:
#     writer = csv.writer(w)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerows([['1', '张三', 18], ['2', 'jack', 21], ['3', 'bob', 24]])

# 读取操作
# with open('data.csv', 'r', encoding='utf-8') as w:
#     reader = csv.reader(w)
#     for i in reader:
#         print(i)


# 动作链
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from time import sleep


# web = webdriver.Chrome('/usr/local/bin/chromedriver')
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# web.get(url)

# web.switch_to.frame('iframeResult')

# source = web.find_element_by_css_selector('#draggable')

# # .以css的方式等为class #以css的方式定位id
# target = web.find_element_by_css_selector('#droppable')

# actions = ActionChains(web)
# actions.drag_and_drop(source, target)
# actions.perform()

# sleep(5)

# 两个方法破解
'''
1. 自己写一个
2. 引用别人写好的包
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 小于88版本
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#         navigator.webdriver = undefined
#         Object.defineProperty(navigator,'webdriver',{
#         get:()=>undefined
#         })
#     """
# }
# )

# 大于88版本的
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

web.get('https://www.baidu.com')

time.sleep(10)
