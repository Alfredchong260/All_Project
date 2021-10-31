"""
目标网址:https://music.163.com/#/playlist?id=924680166

要求:
	1. 使用selenium
	2. 爬取前面5页的评论数据保存为txt文件

"""

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from tqdm import  tqdm
from time import sleep

url = 'https://music.163.com/#/playlist?id=924680166'

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
drive.implicitly_wait(10)

drive.get(url)
drive.switch_to.frame(0)
drive.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def formatter(com):
    return f"用户名：{com.split('：')[0]}\n评论：{com.split('：')[1]}\n\n"

with open('网易云评论.txt', 'w', encoding='utf-8') as w:
    for i in range(10):
        comments = drive.find_elements_by_css_selector('.itm')
        for comment in tqdm(comments, desc=f'正在爬取第{i + 1}页评论'):
            com = comment.find_element_by_css_selector('.cnt.f-brk').text
            info = formatter(com)
            w.write(info)

        drive.find_element_by_link_text('下一页').click()
        sleep(3)

input()
drive.quit()
