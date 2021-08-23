# 知足的喷瓜

'''
    全局思路：
        得到所有视频链接
        二次访问
        进入所有评论
        得到所有评论
        将数据整合写入txt文档
    问题：
        1. 每一条视频的评论的页数都不同
        2. 评论太多,高达数万,全拿下来太耗费时间
    解决方法：
        1. 得到评论的总页数,然后再用for循环确保能得到所有评论
        2. 每条视频最多拿5页评论
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

web = webdriver.Chrome("/usr/local/bin/chromedriver")

wait = WebDriverWait(web, 10)

class douban:

    # 先访问页面得到标题和内层链接
    def main(self):
        web.get("https://movie.douban.com/chart")
        infos =web.find_elements_by_class_name("nbg")
        link = self.getLinks(infos)
        title = self.getTitles(infos)
        comment = self.second_visit(infos)
        first = []
        for l, t in zip(link, title):
            results = self.firstLine(title=t, link=l)
            first.append(results)
        second = []
        for i in comment:
            results = self.secondLine(comment=i)
            second.append(results)

        for f in first:
            for s in second:
                self.writeTXT(first=f, second=s)

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
        comments = []
        links = self.getLinks(infos)
        for link in links:
            web.get(link)
            web.find_element_by_xpath('//*[@id="reviews-wrapper"]/p/a').click()
            time.sleep(2)
            pages = self.goToComment()
            for page in pages:
                page = int(page)
                comments.append(self.getComment(page))

        return comments

    # 确保能访问所有评论的页面
    def goToComment(self):
        pages = []
        try:
            num = web.find_element_by_xpath('//div[@class="paginator"]/a[10]')
            pages.append(num.get_property('textContent'))

        except Exception:
            try:
                num = web.find_element_by_xpath('//div[@class="paginator"]/a[9]')
                pages.append(num.get_property('textContent'))

            except Exception:
                try:
                    num = web.find_element_by_xpath('//div[@class="paginator"]/a[5]')
                    pages.append(num.get_property('textContent'))

                except Exception:
                    num = web.find_element_by_xpath('//div[@class="paginator"]/a[2]')
                    pages.append(num.get_property('textContent'))

        return pages

    # 根据评论的总页数爬取所有评论
    def getComment(self, page):
        all = []
        if page > 5:
            for i in range(5):
                comments = web.find_elements_by_class_name('review-short')
                for comment in comments:
                    all.append('\n'.join(comment.get_attribute('textContent').split()).replace("\n", " "))
                    print('\n'.join(comment.get_attribute('textContent').split()).replace("\n", " "))
                    time.sleep(2)

                try:
                    web.find_element_by_class_name("next").click()

                except Exception:
                    pass

        else:
            for i in range(page):
                comments = web.find_elements_by_class_name('review-short')
                for comment in comments:
                    all.append('\n'.join(comment.get_attribute('textContent').split()).replace("\n", " "))
                    print('\n'.join(comment.get_attribute('textContent').split()).replace("\n", " "))
                    time.sleep(2)

                try:
                    web.find_element_by_class_name("next").click()

                except Exception:
                    pass

        return all

    def firstLine(self, title, link):
        format = "电影名:{}\t电影链接:{}".format(title, link)

        return format
        
    def secondLine(self, comment):
        format = "评论:{}\n".format(comment)

        return format

    def writeTXT(self, first, second):
        with open("豆瓣电影评分.txt", "a+") as f:
            f.write(first + "\n")
            for i in second:
                f.write(i)

if __name__ == "__main__":
    test = douban()
    test.main()
