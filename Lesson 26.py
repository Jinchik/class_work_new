# Пирамида тестирования
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF

driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')
driver = webdriver.Firefox(service=driver_path_firefox)
driver.maximize_window()
url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'
driver.get(url)
q1_fullxpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1_xpath = '//input[@name = "q1"]'
q1 = driver.find_element('xpath',q1_xpath)
q1.send_keys('some')
q9_a_fullxpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
q9_a_xpath ='//input[@name = "q9" and @value = "a"]'
q9_a = driver.find_element('xpath',q9_a_xpath)
q9_a.click()
q19_a_fullxpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
q19_a_xpath = '//input[@name = "q19" and @value = "a"]'
q19_a = driver.find_element('xpath',q19_a_xpath)
q19_a.click()
q2_fullxpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[3]/td[3]/input'
q2_xpath = '//input[@name = "q2"]'
q2 = driver.find_element('xpath', q2_xpath)
q2.send_keys('answer')
q10_b_fullxpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[4]/td[3]/input'
q10_xpath = '//input[@name = "q10" and @value = "b"]'
q10_b = driver.find_element('xpath',q10_xpath)
q10_b.click()
q20_b_fullxpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[4]/td[3]/input'
q20_xpath = '//input[@name = "q20" and @value = "b"]'
q20_b = driver.find_element('xpath',q20_xpath)
q20_b.click()
