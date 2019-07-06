from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')


def log_to_facebook():
    driver.get('https://www.facebook.com/')
    email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
    email_element.send_keys('maheen@northsouth.edu')
    pass_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
    pass_element.send_keys('abecoeasd')
    elem = driver.find_element(By.XPATH, '//*[@id="u_0_2"]')
    elem.click()


def log_to_github():
    driver.get('https://github.com/')
    sign_in_element = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    sign_in_element.click()
    username_element = driver.find_element_by_xpath('//*[@id="login_field"]')
    username_element.send_keys('mustavi.maheen@northsouth.edu')
    password_element = driver.find_element_by_xpath('//*[@id="password"]')
    password_element.send_keys('Porosh11')
    log_in_element = driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[3]/input[4]')
    log_in_element.click()


log_to_github()
