import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://pgu-uat-fed.test.gosuslugi.ru/600316/1/form"
driver.get(url)

driver.implicitly_wait(10)

element = driver.find_element(By.ID, 'login')
element.send_keys('000-729-729 38')

element = driver.find_element(By.ID, 'password')
element.send_keys('11111111')

loginButton = driver.find_element(By.CLASS_NAME, 'plain-button')
loginButton.click()

time.sleep(3)

userButton = driver.find_element(By.CLASS_NAME, '-ms-row-lg-1')
userButton.click()

time.sleep(3)

userStart = driver.find_element(By.CLASS_NAME, 'button')
userStart.click()

time.sleep(3)

driver.close()