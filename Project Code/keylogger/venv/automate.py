from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
driver.get('https://www.facebook.com/')
emailElement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailElement.send_keys('01622330898')
passElement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passElement.send_keys('Porosh11.7!@')

elem = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
elem.click()
