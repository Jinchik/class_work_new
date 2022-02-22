# Пирамида тестирования
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF

driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')
driver = webdriver.Firefox(service=driver_path_firefox)
driver.maximize_window()
url = 'https://dumskaya.net/'
driver.get(url)

enter_xpath = '//a[@id="pp"]'
enter = driver.find_element('xpath',enter_xpath)
enter.click()