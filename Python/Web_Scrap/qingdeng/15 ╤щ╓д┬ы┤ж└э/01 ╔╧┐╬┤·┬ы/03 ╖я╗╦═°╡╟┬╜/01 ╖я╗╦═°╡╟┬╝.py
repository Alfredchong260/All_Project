# requests模块, 每一次请求默认都是单次请求
import base64

from selenium import webdriver
import time
from constants import FENG_USERNAME, FENG_PASSWORD


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.ifeng.com/')
driver.implicitly_wait(10)
driver.maximize_window()


"""找到账号点击登录"""
driver.find_element_by_css_selector('.login_in_2x-3NxtSKIw').click()
time.sleep(3)

"""注意嵌套网页"""
iframe_label = driver.find_element_by_css_selector('.box-1pZSPyeN>div:nth-child(2)>iframe')
driver.switch_to.frame(iframe_label)

driver.find_element_by_css_selector('.tab-2sXGklBv>span:nth-child(1)').click() # 点击账号登录
time.sleep(3)


"""输入用户信息"""
username_input = driver.find_element_by_css_selector('.loginById-3HzkdnTl>div>div:nth-child(1)>input')
username_input.send_keys(FENG_USERNAME)
time.sleep(1)

pwd_input = driver.find_element_by_css_selector('.loginById-3HzkdnTl>div>div:nth-child(2)>div>div>input')
pwd_input.send_keys(FENG_PASSWORD)
time.sleep(1)


"""验证码的处理"""
# 保存验证码
img_label = driver.find_element_by_css_selector('.codeImg-2pONyHUT>img')
img_str = img_label.get_attribute('src')
print('处理之前的验证码图片:', img_str)
base64_str = img_str.split(',')[1]
print('处理以后的验证码图片:', base64_str)

# 把字符串形式的图片保存
img_bytes = base64.b64decode(base64_str)
with open('yzm.png', mode='wb') as f:
    f.write(img_bytes)
    print('验证码保存完毕')

"""调用打码平台识别验证码"""
from img_api import base64_api
result = base64_api('yzm.png')
print('验证码识别结果:', result)

"""输入验证码"""
yzm_label = driver.find_element_by_css_selector('.loginById-3HzkdnTl>div>div:nth-child(3)>div>div>div>input')
yzm_label.send_keys(result)


"""点击登录按钮"""
time.sleep(1)
driver.find_element_by_css_selector('.submmitBtn-2AmMFR0C').click()


input()
driver.quit()