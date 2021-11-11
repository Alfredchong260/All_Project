# requests模块, 每一次请求默认都是单次请求
import base64

from selenium import webdriver
import time
from constants import BILIBILI_USERNAME, BILIBILI_PASSWORD


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(10)
driver.maximize_window()


"""输入用户信息"""
username_input = driver.find_element_by_css_selector('#login-username')
username_input.send_keys(BILIBILI_USERNAME)
time.sleep(1)

pwd_input = driver.find_element_by_css_selector('#login-passwd')
pwd_input.send_keys(BILIBILI_PASSWORD)
time.sleep(1)

# 点击登录
driver.find_element_by_css_selector('.btn.btn-login').click()
time.sleep(2)   # 一定要给时间让图片弹出<加载>

"""保存图片"""
img_label = driver.find_element_by_css_selector('.geetest_holder.geetest_silver')  # 找到图片标签
img_label.screenshot('yzm.png')  # 根据标签 页面截图
time.sleep(2)
print('验证码保存完毕!!!')


"""对接打码平台识别验证码"""
from img_api import base64_api

result = base64_api('yzm.png')
print('验证码识别结果: ', result)

# 处理坐标
result_list = result.split('|')  # ['213,162', '98,163', '83,77']

from selenium.webdriver import ActionChains

for res in result_list:
    x = res.split(',')[0]  # x 轴
    y = res.split(',')[1]  # y 轴

    # ActionChains 鼠标动作连对象
    # move_to_element_with_offset  根据页面的元素做点击操作
    ActionChains(driver).move_to_element_with_offset(img_label, int(x), int(y)).click().perform()


# 点击确认
time.sleep(2)
driver.find_element_by_css_selector('.geetest_commit_tip').click()


input()
driver.quit()