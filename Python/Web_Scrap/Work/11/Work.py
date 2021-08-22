# 知足的喷瓜

'''
    全局思路：
        得到所有视频链接
        二次访问
        进入所有评论
        得到所有评论
    问题：
        1. 每一条视频的评论的页数都不同
    解决方法：
        1. 先取得评论总数，再以一个公式来计算总共有多少页的评论
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

web = webdriver.Chrome("/usr/local/bin/chromedriver")

wait = WebDriverWait(web, 10)


class douban:
    def __init__(self):
        pass

    # 先访问页面得到标题和内层链接
    def main(self):
        web.get("https://movie.douban.com/chart")
        infos =web.find_elements_by_class_name("nbg")
        self.getLinks(infos)
        self.getTitles(infos)
        self.second_visit(infos)

    # 将得到的链接整合
    def getLinks(self, infos):
        li = []
        for links in infos:
            link = links.get_property('href')
            li.append(link)

        return li

    # 将得到的标题整合
    def getTitles(self, infos):
        li = []
        for titles in infos:
            title = titles.get_property('title')
            li.append(title)

        return li

    # 访问内层页面并点击到评论区内
    def second_visit(self, infos):
        links = self.getLinks(infos)
        for link in links:
            web.get(link)
            web.find_element_by_xpath('//div[@class="section-discussion"]/p/a').click()
            time.sleep(2)
            self.getToComment()

    def getToComment(self):
        try:
            num = web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/a[10]')
            print(num.get_attribute('textContent'))
        except Exception:
            try:
                num = web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/a[9]')
                print(num.get_attribute('textContent'))
            except Exception:
                num = web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/a[5]')
                print(num.get_attribute('textContent'))

if __name__ == "__main__":
    test = douban()
    print(test.main())
