"""
目标网址: https://www.wjx.cn/jq/87910206.aspx

1.用selenium自动填写问卷, 自动提交
2.单选题随机选一个选项, 多选题随机选三个选项

"""
import re
import time
import random

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
# 配置浏览器的某个属性
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
    })
"""
})

driver.get('https://www.wjx.cn/jq/87910206.aspx')

driver.implicitly_wait(10)

divs = driver.find_elements_by_css_selector('.div_question')
print(divs)
print(len(divs))

"""
单选题: 1 - 10
多选题: 11 - 12
"""

one_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
any_choice = [10, 11]

# 单选题随机选择
for i in one_choice:
    lis = divs[i].find_elements_by_css_selector('ul li')
    random.choice(lis).click()

# 单选题随机选择
for j in any_choice:
    lis = divs[j].find_elements_by_css_selector('ul li')
    # random.choice(lis).click()
    # 随机选取三个
    # random.choices()  # .choices() 选择的多个选项可能会重复
    lis_list = random.sample(lis, k=3)    # 会随机选择不同的元素
    for k in lis_list:
        k.click()

time.sleep(1)
# 提交
driver.find_element_by_css_selector('.submitbutton').click()

time.sleep(1)
driver.find_element_by_css_selector('#alert_box .mainBgColor').click()

time.sleep(1)
driver.find_element_by_css_selector('.sm-ico-wave').click()

input()
driver.quit()

# sleenium检测
