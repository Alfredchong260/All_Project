from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
    有iframe就是嵌套网页
    需要特定代码进入iframe的网页
    才能对嵌套网页进行操作
'''

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

drive.get('https://music.163.com/#/search/m/?s=错位时空&type=1')

# 根据索引进入嵌套网页，索引值是从0开始的
# 第一种进入嵌套网页的方法
drive.switch_to_frame(0)

# 退出嵌套网页,切换成父级网页
drive.switch_to.parent_frame()
print(drive.page_source)

# 第二种进入嵌套网页的方法
iframe = drive.find_element_by_id('g_iframe')
drive.switch_to.frame(iframe)

print(drive.page_source)

'''嵌套网页的进入与退出，最好一级一级去做'''


drive.get('https://github.com/search?q=nvim')
drive.execute_script('window.scrollTo(0, document.body.scrollHeight)')

input()
drive.quit()
