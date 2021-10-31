from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from random import sample
from time import sleep

url = 'https://www.wjx.cn/jq/87910206.aspx'

# 将window.navigator.webdriver修改成false
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local//bin//chromedriver', options=option)

drive.implicitly_wait(10)
drive.get(url)

# 生成随机数，随机数数量根据num的值决定
def random_num(total, num):
    return sample(range(1, total), num)

# 得到所有问题，方便二次操作
questions = drive.find_elements_by_css_selector('.ulradiocheck')

# 遍历所有问题，逐个进行操作
for question in questions:
    # 先确保题目是单选题
    lis = question.find_elements_by_css_selector('.jqRadio')
    # 得到单选题选项的数量
    total = len(lis)
    # 如果不是0,即为单选题
    if total:
        # 此为调用随机数函数，并指定返回值只有一个
        num = random_num(total, 1)
        # 根据返回值选定第几个选项并进行点击
        question.find_element_by_xpath(f'./li[{num[0]}]').click()
    else:
        # 如果发现不是单选题，即为多选题，先进行页面下滑，方便操作
        drive.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # 查找多选题的选项
        li = question.find_elements_by_css_selector('.jqCheckbox')
        # 得到多选题的选项数量
        tol = len(li)
        # 生成随机数，并指定num为3
        nums = random_num(tol, 3)
        # 返回的数据为列表，使用遍历进行逐个点击
        for num in nums:
            question.find_element_by_xpath(f'./li[{num}]').click()

# 此为提交表单的按钮
sleep(1)
drive.find_element_by_css_selector('.submitbutton').click()

# 此为第一次校验按钮
sleep(1)
drive.find_element_by_css_selector('button.mainBgColor').click()

# 此为第二次校验按钮
sleep(1)
drive.find_element_by_css_selector('#rectMask').click()

input()
drive.quit()
