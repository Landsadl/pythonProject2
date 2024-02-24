from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Edge()
browser.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')

rad_button = browser.find_element(By.ID, 'isAgeSelected')
rad_button.click()
time.sleep(2)

rad_button_default = browser.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/div[1]/form/label[2]/input')
rad_button_default.click()
time.sleep(2)

check_all = browser.find_element(By.ID, 'check1')
check_all.click()
time.sleep(1)

uncheck_all = browser.find_element(By.ID, 'check1')
uncheck_all.click()

time.sleep(25)

