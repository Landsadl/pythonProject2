from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Edge()
browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

elem = browser.find_element(By.ID, 'user-message')
elem.clear()
elem.send_keys('This is coolish')
time.sleep(5)

show_message_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
assert 'Show Message' in browser.page_source
show_message_button.click()


summing1 = browser.find_element(By.NAME, 'sum1')
summing1.send_keys(int(5))
summing2 = browser.find_element(By.NAME, 'sum2')
summing2.send_keys(int(6))
time.sleep(5)

adding = browser.find_element(By.CSS_SELECTOR, '#gettotal > .btn')
adding.click()

time.sleep(45)

