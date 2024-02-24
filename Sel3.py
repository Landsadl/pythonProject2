from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Edge()
browser.get('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html')

drop_down = browser.find_element(By.ID, 'select-demo')
drop_down.click()

selection = Select(drop_down)

selection.select_by_value('Monday')

drop_down2 = browser.find_element(By.ID, 'multi-select')
drop_down2_select= Select(drop_down2)
drop_down2_select.select_by_value('Florida')
drop_down2_select.select_by_value('Ohio')

first_select = browser.find_element(By.ID, 'printMe')
first_select.click()
time.sleep(2)
all_select = browser.find_element(By.ID, 'printAll')
all_select.click()



time.sleep(25)