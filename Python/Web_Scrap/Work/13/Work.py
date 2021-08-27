# 知足的喷瓜

'''
    全局思路：
        前往目标网页
        通过验证码
'''

from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
action = ActionChains(web)
chaojiying = Chaojiying_Client('tzputuan', 'tzputuan', '921722')

web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        navigator.webdriver = undefined
        Object.defineProperty(navigator,'webdriver',{
        get:()=>undefined
        })
    """
}
)

# 到登陆网页
web.get('https://kyfw.12306.cn/otn/resources/login.html')
sleep(2)

# 跳转到指定页面
web.find_element_by_class_name('login-hd-account').click()
web.find_element_by_id('J-userName').send_keys('123456')
web.find_element_by_id('J-password').send_keys('123456789')
sleep(2)

# 得到验证的照片
img = web.find_element_by_id('J-loginImgArea').screenshot_as_png
sleep(2)

# 以超级鹰来解析验证码并得到答案
dic = chaojiying.PostPic(img ,9004)
result = dic['pic_str']
li = result.split('|')
for i in li:
    temp = i.split(',')
    x = int(temp[0])
    y = int(temp[1])
    action.move_to_element_with_offset(img, x, y).click().perform()

sleep(5)

# 进行登陆的操作
web.find_element_by_class_name('login-btn').click()
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
