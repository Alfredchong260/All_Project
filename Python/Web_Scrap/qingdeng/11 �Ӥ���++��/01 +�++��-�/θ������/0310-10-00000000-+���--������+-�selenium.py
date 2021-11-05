"""
目标网址:https://music.163.com/#/playlist?id=924680166

要求:
	1. 使用selenium
	2. 爬取前面5页的评论数据保存为txt文件

"""
import re
import time

from selenium import  webdriver


def parse_data():
    """解析数据并保存"""
    divs = driver.find_elements_by_css_selector('.itm')

    for div in divs:
        cnt = div.find_element_by_css_selector('.cnt.f-brk').text
        # print(cnt)
        cnt = cnt.replace('\n', '')
        cnt = re.findall('：(.*)', cnt, re.S)[0]
        print(cnt)
        with open('contend.txt', mode='a', encoding='utf-8') as f:
            f.write(cnt + '\n')


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://music.163.com/#/playlist?id=924680166')

driver.implicitly_wait(10)
driver.switch_to.frame(0)  # 进入嵌套网页
# print(driver.page_source)

for page in range(5):  # 01234
    # 下拉一定要进去嵌套网页, 每一页都要下拉
    js = "document.documentElement.scrollTop=document.documentElement.scrollHeight"
    driver.execute_script(js)
    # 解析评论数据
    parse_data()

    # 点击下一页
    driver.find_element_by_css_selector('.zbtn.znxt').click()
    time.sleep(2)



input()
driver.quit()


