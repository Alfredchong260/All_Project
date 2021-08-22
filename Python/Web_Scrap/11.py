from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

web = webdriver.Chrome("/usr/local/bin/chromedriver")
web.get("https://movie.douban.com/chart")
# print(web.page_source)

# 获取单个元素, 成功则继续
# title = web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[1]/a')
# print(title.get_property('title'))
# print(title.get_property('href'))

wait = WebDriverWait(web, 10)

links = []
titles = []
# 获取多个元素
infos = web.find_elements_by_class_name("nbg")
# print(infos)
for href in infos:
    links.append(href.get_property('href'))
    # i = href.get_property('href')
    # web.get(i)

for title in infos:
    titles.append(title.get_property('title'))

for link in links:
    web.get(link)
    comments = web.find_elements_by_xpath('//div[@class="main review-item"]//div[@class="short-content"]')
    # for comment in comments:
    #     print("\n".join(comment.get_property('textContent').split()))
