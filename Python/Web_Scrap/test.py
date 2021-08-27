'''
全局思路：
    筛选需要的数据
    把各自的数据分开记录
    将数据分别写入txt文档
'''
from logging import info
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class baidu:

    # 先访问页面
    def main(self):
        web.get(url)
        self.infos()

    # 筛选所有需要的数据
    def infos(self):
        results = web.find_elements_by_class_name('para')
        time.sleep(2)
        names = web.find_elements_by_class_name('albumName')
        dates = web.find_elements_by_class_name('albumDate')
        movieName = web.find_elements_by_xpath('//div[@class="info"]/p/b[1]')
        movieDate = web.find_elements_by_xpath('//div[@class="info"]/p/b[2]')

        info = self.getResults(results)
        formattedNateDate = []
        formattedMovieData = []

        for i, j in zip(self.getNames(names), self.getDates(dates)):
            a = self.formatForNameDate(name=i, date=j)
            formattedNateDate.append(a)

        for i, j in zip(self.getMovieName(movieName), self.getMovieDate(movieDate)):
            b = self.formatMovieData(name=i, date=j)
            formattedMovieData.append(b)

        for i in info:
            self.writeData(data=i)

        for j in formattedNateDate:
            self.writeData(data=j)

        for k in formattedMovieData:
            self.writeData(data=k)

    def getResults(self, results):
        li = []
        for result in results:
            a = '\n'.join(result.get_property('textContent').split())
            li.append(a)

        return li

    def getNames(self, names):
        li = []
        for name in names:
            li.append(name.get_property('textContent'))
            
        return li

    def getDates(self, dates):
        li = []
        for date in dates:
            li.append(date.get_property('textContent'))
        
        return li

    def getMovieName(self, movieName):
        li = []
        for name in movieName:
            li.append(name.get_property('textContent'))
        
        return li

    def getMovieDate(self, movieDate):
        li = []
        for date in movieDate:
            li.append(date.get_property('textContent'))
        
        return li

    def formatForNameDate(self, name, date):
        format = '''专辑名称：{}\n发放日子：{}\n\n'''.format(name, date)

        return format

    def formatMovieData(self, name, date):
        format = '''电影名字：{}\n发行日子：{}\n\n'''.format(name, date)

        return format

    def formatForResults(self):
        pass

    def writeData(self, data):
        with open('数据.txt', 'a+') as w:
            w.write(data)

while True:
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')

    web = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
    choice = input('请输入你要查找的明星：')
    if choice.lower() == 'q':
        break

    url = 'https://baike.baidu.com/item/' + choice
    test = baidu()
    test.main()
    web.close()
