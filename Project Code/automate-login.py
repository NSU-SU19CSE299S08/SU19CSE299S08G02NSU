from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
driver.get('https://www.facebook.com/')
emailElement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailElement.send_keys('maheen@northsouth.edu')
passElement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passElement.send_keys('abecoeasd')

elem = driver.find_element(By.XPATH, '//*[@id="u_0_2"]')
elem.click()
