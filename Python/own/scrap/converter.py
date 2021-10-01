from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)
wait = WebDriverWait(web, timeout=5)

class YouTubeConverter:
    def __init__(self, url, type):
        self.url = url
        self.type = type

    def main(self):
        self.check()

    def downloadVideo(self):
        web.get('https://ytmp3.cc/en17/')
        if self.type.upper() == 'MP3':
            web.find_element(By.ID, 'mp3').click()
        else:
            web.find_element(By.ID, 'mp4').click()

        web.find_element(By.ID, 'input').send_keys(self.url)
        sleep(2)
        web.find_element(By.ID, 'submit').click()
        sleep(2)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#buttons')))
        web.find_element(By.XPATH, '//div[@id="buttons"]/a[1]').click()
        sleep(5)

    def check(self):
        type = self.type
        if type.upper() == 'MP3' or type.upper() == 'MP4':
            self.downloadVideo()
        else:
            print('你所选择的格式不支持，请重新输入')


if __name__ == '__main__':
    while True:
        url = input('请输入要转换的链接：')
        if url.upper() == 'Q':
            print('感谢使用')
            break
        else:    
            type = input('请选择格式 MP4/MP3：')
            test = YouTubeConverter(url, type)
            test.main()
