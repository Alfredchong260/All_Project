from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select    # 下拉框的功能
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

drive.implicitly_wait(10)

drive.get('https://www.jq22.com/demo/shengshiliandong/')

'''鼠标动作链实现'''

# 创建一个动作链对象，传入浏览器对象
# 定义一个动作
# 执行这个动作

select = drive.find_element_by_css_selector('#s_province')
sel = Select(select)
sel.select_by_index(2)
sleep(2)
sel.select_by_value('河北省')
sleep(2)
sel.select_by_visible_text('黑龙江省')
sleep(2)

'''处理弹窗'''
drive.switch_to_alert() # 切换弹窗

input()
drive.quit()
