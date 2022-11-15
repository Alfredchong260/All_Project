import undetected_chromedriver as UC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import time
from selenium import webdriver

# options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certifications-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# Open link
driver = UC.Chrome(use_subprocess=True)
driver.get("https://forms.gle/x2XfYQsaUiCkV4Th8")
wait = WebDriverWait(driver, 30)

username = "affredchong@gmail.com"
password = "Chong8182"

Next = driver.find_element(By.ID, "identifierNext")
Next.click()
wait.until(EC.visibility_of_element_located(
    (By.ID, "identifierId"))).send_keys(username)
Next.click()
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))).send_keys(password)
passwordnext = driver.find_element(By.ID, "passwordNext")
passwordnext.click()

sleep(5)


data = pd.read_csv("./test-web-fill-form.csv")
for i in range(0, len(data)):
    print(i)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    name_field = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.send_keys(data.iloc[i, 0])
    sleep(0.5)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')))
    status_field = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
    status_field.click()
    sleep(0.5)
    MR = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/span'
    MRS = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]/span'
    if data.iloc[i, 1] == 'MR':
        wait.until(EC.visibility_of_element_located((By.XPATH, MR)))
        select_gender = driver.find_element(By.XPATH, MR).click()
        sleep(0.5)
    else:
        wait.until(EC.visibility_of_element_located((By.XPATH, MRS)))
        select_gender = driver.find_element(By.XPATH, MRS).click()
        sleep(0.5)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    IC_field = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    IC_field.send_keys(str(data.iloc[i, 2]))
    sleep(0.5)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    phone_number_field = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    phone_number_field.send_keys(str(data.iloc[i, 3]))
    sleep(0.5)

    address = data.iloc[i, 4].split(",")
    address_street_field = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_block_field = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_postal_field = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_street_field.send_keys(address[0])
    address_block_field.send_keys(address[1])
    address_postal_field.send_keys(address[2])
    sleep(0.5)

    single = '//*[@id="i37"]/div[3]/div'
    married = '//*[@id="i40"]/div[3]/div'
    if data.iloc[i, 5] == 'married':
        wait.until(EC.visibility_of_element_located((By.XPATH, single)))
        driver.find_element(By.XPATH, married).click()
        sleep(0.5)
    else:
        wait.until(EC.visibility_of_element_located((By.XPATH, married)))
        driver.find_element(By.XPATH, single).click()
        sleep(0.5)

    # upload PDF
    # wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[2]/span/span[2]')))
    # driver.find_element(
    #     By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[2]/span/span[2]').click()

    sleep(3)

    # Switching to iframe
    # driver.switch_to.frame(driver.find_elements(
    #     By.CSS_SELECTOR, '.picker-dialog-content.fFW7wc-OEVmcd > iframe')[0])
    # print("Successfully switch to iframe")

    wait.until(EC.visibility_of_element_located((By.XPATH, '//html/body/div/div[2]/form/div[2]/div/div[3]/div/div/div/span/span')))
    driver.find_element(By.XPATH, "//html/body/div/div[2]/form/div[2]/div/div[3]/div/div/div/span/span").click()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//html/body/div/div[2]/div/div/div[4]/a')))
    driver.find_element(By.XPATH, '//html/body/div/div[2]/div/div/div[4]/a').click()
    # driver.find_element(By.CSS_SELECTOR, ".EeNpqb > input[type='file']").send_keys("/home/cms/working/SYAD-Exam.png")
    # break

