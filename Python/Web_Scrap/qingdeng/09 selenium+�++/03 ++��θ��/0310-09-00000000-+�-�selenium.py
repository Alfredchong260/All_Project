"""
目标网址: https://www.ku6.com/detail/71

作业要求:
    1.用 selenium 采集所需要的数据
    2.需要数据如下所示
        title 视频的标题
        img_url 视频图片对应的url地址
        detail_url 视频详情页url地址
    3.保存为csv数据
请在下方编写代码
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from tqdm import tqdm
import time
import csv

url = 'https://www.ku6.com/detail/71'

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

drive.get(url)

fieldname = ['Title', 'Img_url', 'Detail_url']

with open('酷6.csv', 'w', encoding='utf-8') as w:
    csv_writer = csv.DictWriter(w, fieldnames=fieldname)
    csv_writer.writeheader()
    for i, count in enumerate(range(0, 400, 40)):
        div_tag = drive.find_elements_by_class_name('video-item')[count:]
        for div in tqdm(div_tag, desc=f'正在爬取第{i + 1}页数据'):
            link = div.find_element_by_class_name('video-image-warp').get_attribute('href')
            img = div.find_element_by_xpath('./div[1]/a/img').get_attribute('src')
            title = div.find_element_by_xpath('./div[2]/h3/a').text
            csv_writer.writerow({
                'Title': title,
                'Img_url': img,
                'Detail_url': link
            })

        time.sleep(1)
        drive.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        drive.find_element_by_css_selector('.load-more>img').click()

        time.sleep(2)

input()
drive.quit()
