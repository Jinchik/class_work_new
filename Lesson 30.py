from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from XPATH import home_page


#Task 1
driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua/ua/productstoorder')
driver.maximize_window()
#2Task 2
home_ru = '/html/body/div[1]/div[2]/div/div/div/ul/li[1]/a'
home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_ru)
    )
)
home_ru_button.click()
# Task3
product_ru = '/html/body/div[1]/div[2]/div/div/div/ul/li[2]/a'
product_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, product_ru)
    )
)
product_ru_button.click()
# Task 4
logo = '//img[@src="http://yanigen.com.ua/images/logo-2015.png"]'
WebDriverWait(driver, 100).until_not(
    EC.presence_of_element_located(
        (By.XPATH, logo)
    )
)
driver.quit()