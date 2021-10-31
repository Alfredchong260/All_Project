from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

drive = webdriver.Chrome('/usr/local/bin/chromedriver', options=option)

drive.get('https://github.com/search?q=nvim')

time.sleep(2)

drive.execute_script('var q=document.documentElement.scrollTop=1000')

drive.find_element_by_class_name('next_page').click()

time.sleep(5)

drive.execute_script('var q=document.documentElement.scrollTop=1000')

drive.find_element_by_class_name('next_page').click()

time.sleep(5)
