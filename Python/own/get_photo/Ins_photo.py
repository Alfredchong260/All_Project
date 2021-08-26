'''
全局思路：
    得到链接以便能进行接下来的数据爬取
    将得到的链接二次处理得到内层数据
    将内层数据下载成jpg
'''

from selenium import webdriver
import time

driver = webdriver.Firefox("/usr/local/bin")

class ins:

    def main(self):
        driver.get("https://www.instagram.com/sooyaaa__/")
        time.sleep(3)
        try: 
            self.logIn()
            self.findWebsite()
        except Exception:
            pass
        self.visitPhoto()

    def logIn(self):
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("affredchong@gmail.com")
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Chong6260")
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(3)
        driver.find_element_by_class_name("cmbtv").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        time.sleep(3)

    def findWebsite(self):
        driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div').send_keys('sooyaaa__')
        time.sleep(3)
        
    def visitPhoto(self):
        links = driver.find_elements_by_tag_name("a")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 300)")
        time.sleep(2)
        for link in links:
            print(link.get_attribute("href"))

if __name__ == "__main__":
    test = ins()
    test.main()

