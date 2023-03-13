from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

username = 'FADHILAH'
password = 'Motosing123#'


driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)

wait = WebDriverWait(driver, 20)
url = 'https://bizpro.aeoncredit.com.my/acs-os/merchant/login'

driver.get(url)

username_xpath = '/html/body/div/div[2]/form/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/div/input[1]'
password_path = '/html/body/div/div[2]/form/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/div/input[2]'
btn_xpath = '/html/body/div/div[2]/form/div/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/div/div/div/button'

wait.until(expected_conditions.presence_of_element_located((By.XPATH, username_xpath)))
driver.find_element(By.XPATH, username_xpath).send_keys(username)

wait.until(expected_conditions.presence_of_element_located((By.XPATH, password_path)))
driver.find_element(By.XPATH, password_path).send_keys(password)

wait.until(expected_conditions.presence_of_element_located((By.XPATH, btn_xpath)))
driver.find_element(By.XPATH, btn_xpath).click()

close_btn = '/html/body/div[1]/div[2]/form/div[1]/div/div/div[3]/button'
wait.until(expected_conditions.presence_of_element_located((By.XPATH, close_btn)))
driver.find_element(By.XPATH, close_btn).click()

sleep(3)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#cancel')))
driver.find_element(By.CSS_SELECTOR,'#cancel').click()

a_link = '/html/body/div/div[1]/div/div[3]/div/ul/li[6]/a'
wait.until(expected_conditions.presence_of_element_located((By.XPATH, a_link)))
driver.find_element(By.XPATH, a_link).click()

skip_btn = '//html/body/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/button'
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, skip_btn)))
# driver.find_element(By.XPATH, skip_btn).click()


input()