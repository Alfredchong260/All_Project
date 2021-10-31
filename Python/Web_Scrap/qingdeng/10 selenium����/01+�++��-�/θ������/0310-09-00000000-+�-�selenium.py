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
import csv

from selenium import webdriver


# 1. 创建一个浏览器对象
driver = webdriver.Chrome(executable_path='chromedriver.exe')


# 2. 执行自动化操作
driver.get('https://www.ku6.com/detail/71')
driver.maximize_window()
driver.implicitly_wait(10)

# driver.page_source 查看浏览器获取的html数据
# print(driver.page_source)

# driver.page_source 得到的数据是 html?  parsel
# selenium 数据解析
divs = driver.find_elements_by_css_selector('.container .video-item-warp.m-t-sm>div>div')
# print(divs)
# print(len(divs))

for div in divs:
    title = div.find_element_by_css_selector('h3 a').text
    img_url = div.find_element_by_css_selector('div a img').get_attribute('src')
    detail_url = div.find_element_by_css_selector('div a').get_attribute('href')
    print(title, img_url, detail_url)

    # 构造字典对象
    # csv.DictWriter()
    # csv_writer.写表头
    # 可以用普通方式写表头  f.write()

    with open('视频.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([title, img_url, detail_url])
        # csv_writer.


# 3. 退出浏览器
input()  # 阻塞
driver.quit()





