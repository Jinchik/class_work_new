import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')

driver = webdriver.Firefox(service=driver_path_firefox)
#driver = webdriver.Chrome(service=driver_path_chrome)
# url = 'https://core.telegram.org/'
# driver.get(url)
# driver.set_window_position(1600,300)#Для второго монитора расположенного справа
time.sleep(2)
driver.maximize_window()
#HEADLESS БЕЗГОЛОВЫЙ Режим работы без визуального запуска
# driver.set_window_size(300,100)
url = 'https://test.mensa.no/'
driver.get(url)
print(driver.title)
button_18_50_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
# button_51_60_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'
# button_51_60 = driver.find_element('xpath',button_51_60_xpath)
# print(button_51_60.text)
button_18_50 = driver.find_element('xpath',button_18_50_xpath)
print(button_18_50.text)
time.sleep(2)
button_18_50.click()
# button_start_xpath = '//*[@id="startTest"]'
button_start_xpath_full = '/html/body/div[2]/main/cach/div[2]/div/div/div/div[2]/button'
button_start = driver.find_element('xpath',button_start_xpath_full)
button_start.click()
time.sleep(2)
ex1_a_xpath ='/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex1 = driver.find_element('xpath',ex1_a_xpath)
button_ex1.click()
time.sleep(2)
ex2_b_xpath ='/html/body/div[2]/main/cach/div[3]/div[2]/div[3]/div[2]/div/img'
button_ex2 = driver.find_element('xpath',ex2_b_xpath)
button_ex2.click()
time.sleep(2)
ex3_c_xpath ='/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex3 = driver.find_element('xpath',ex3_c_xpath)
button_ex3.click()
time.sleep(2)
ex4_d_xpath ='/html/body/div[2]/main/cach/div[3]/div[4]/div[3]/div[4]/div/img'
button_ex4 = driver.find_element('xpath',ex4_d_xpath)
button_ex4.click()
time.sleep(2)
ex5_e_xpath ='/html/body/div[2]/main/cach/div[3]/div[5]/div[3]/div[5]/div/img'
button_ex5 = driver.find_element('xpath',ex5_e_xpath)
button_ex5.click()
time.sleep(2)
ex6_f_xpath ='/html/body/div[2]/main/cach/div[3]/div[6]/div[3]/div[6]/div/img'
button_ex6 = driver.find_element('xpath',ex6_f_xpath)
button_ex6.click()
time.sleep(2)
ex7_a_xpath ='/html/body/div[2]/main/cach/div[3]/div[7]/div[3]/div[1]/div/img'
button_ex7 = driver.find_element('xpath',ex7_a_xpath)
button_ex7.click()
time.sleep(2)
ex8_b_xpath ='/html/body/div[2]/main/cach/div[3]/div[8]/div[3]/div[2]/div/img'
button_ex8 = driver.find_element('xpath',ex8_b_xpath)
button_ex8.click()
time.sleep(2)
ex9_c_xpath ='/html/body/div[2]/main/cach/div[3]/div[9]/div[3]/div[3]/div/img'
button_ex9 = driver.find_element('xpath',ex9_c_xpath)
button_ex9.click()
time.sleep(2)
ex10_d_xpath ='/html/body/div[2]/main/cach/div[3]/div[10]/div[3]/div[4]/div/img'
button_ex10 = driver.find_element('xpath',ex10_d_xpath)
button_ex10.click()
time.sleep(2)
ex11_e_xpath ='/html/body/div[2]/main/cach/div[3]/div[11]/div[3]/div[5]/div/img'
button_ex11 = driver.find_element('xpath',ex11_e_xpath)
button_ex11.click()
time.sleep(2)
ex12_f_xpath ='/html/body/div[2]/main/cach/div[3]/div[12]/div[3]/div[5]/div/img'
button_ex12 = driver.find_element('xpath',ex12_f_xpath)
button_ex12.click()
time.sleep(2)
ex13_a_xpath ='/html/body/div[2]/main/cach/div[3]/div[13]/div[3]/div[1]/div/img'
button_ex13 = driver.find_element('xpath',ex13_a_xpath)
button_ex13.click()
time.sleep(2)
ex14_b_xpath ='/html/body/div[2]/main/cach/div[3]/div[14]/div[3]/div[2]/div/img'
button_ex14 = driver.find_element('xpath',ex14_b_xpath)
button_ex14.click()
time.sleep(2)
ex15_c_xpath ='/html/body/div[2]/main/cach/div[3]/div[15]/div[3]/div[3]/div/img'
button_ex15 = driver.find_element('xpath',ex15_c_xpath)
button_ex15.click()
time.sleep(2)
ex16_d_xpath ='/html/body/div[2]/main/cach/div[3]/div[16]/div[3]/div[4]/div/img'
button_ex16 = driver.find_element('xpath',ex16_d_xpath)
button_ex16.click()
time.sleep(2)
ex17_e_xpath ='/html/body/div[2]/main/cach/div[3]/div[17]/div[3]/div[5]/div/img'
button_ex17 = driver.find_element('xpath',ex17_e_xpath)
button_ex17.click()
time.sleep(2)
ex18_f_xpath ='/html/body/div[2]/main/cach/div[3]/div[18]/div[3]/div[5]/div/img'
button_ex18 = driver.find_element('xpath',ex18_f_xpath)
button_ex18.click()
time.sleep(2)
ex19_a_xpath ='/html/body/div[2]/main/cach/div[3]/div[19]/div[3]/div[1]/div/img'
button_ex19 = driver.find_element('xpath',ex19_a_xpath)
button_ex19.click()
time.sleep(2)
ex20_b_xpath ='/html/body/div[2]/main/cach/div[3]/div[20]/div[3]/div[2]/div/img'
button_ex20 = driver.find_element('xpath',ex20_b_xpath)
button_ex20.click()
time.sleep(2)
ex21_c_xpath ='/html/body/div[2]/main/cach/div[3]/div[21]/div[3]/div[3]/div/img'
button_ex21 = driver.find_element('xpath',ex21_c_xpath)
button_ex21.click()
time.sleep(2)
ex22_d_xpath ='/html/body/div[2]/main/cach/div[3]/div[22]/div[3]/div[4]/div/img'
button_ex22 = driver.find_element('xpath',ex22_d_xpath)
button_ex22.click()
time.sleep(2)
ex23_e_xpath ='/html/body/div[2]/main/cach/div[3]/div[23]/div[3]/div[5]/div/img'
button_ex23 = driver.find_element('xpath',ex23_e_xpath)
button_ex23.click()
time.sleep(2)
ex24_f_xpath ='/html/body/div[2]/main/cach/div[3]/div[24]/div[3]/div[6]/div/img'
button_ex24 = driver.find_element('xpath',ex24_f_xpath)
button_ex24.click()
time.sleep(2)
ex25_a_xpath ='/html/body/div[2]/main/cach/div[3]/div[25]/div[3]/div[1]/div/img'
button_ex25 = driver.find_element('xpath',ex25_a_xpath)
button_ex25.click()
time.sleep(2)
ex26_b_xpath ='/html/body/div[2]/main/cach/div[3]/div[26]/div[3]/div[2]/div/img'
button_ex26 = driver.find_element('xpath',ex26_b_xpath)
button_ex26.click()
time.sleep(2)
ex27_c_xpath ='/html/body/div[2]/main/cach/div[3]/div[27]/div[3]/div[3]/div/img'
button_ex27 = driver.find_element('xpath',ex27_c_xpath)
button_ex27.click()
time.sleep(2)
ex28_d_xpath ='/html/body/div[2]/main/cach/div[3]/div[28]/div[3]/div[4]/div/img'
button_ex28 = driver.find_element('xpath',ex28_d_xpath)
button_ex28.click()
time.sleep(2)
ex29_e_xpath ='/html/body/div[2]/main/cach/div[3]/div[29]/div[3]/div[5]/div/img'
button_ex29 = driver.find_element('xpath',ex29_e_xpath)
button_ex29.click()
time.sleep(2)
ex30_f_xpath ='/html/body/div[2]/main/cach/div[3]/div[30]/div[3]/div[5]/div/img'
button_ex30 = driver.find_element('xpath',ex30_f_xpath)
button_ex30.click()
time.sleep(2)
ex31_a_xpath ='/html/body/div[2]/main/cach/div[3]/div[31]/div[3]/div[1]/div/img'
button_ex31 = driver.find_element('xpath',ex31_a_xpath)
button_ex31.click()
time.sleep(2)
ex32_b_xpath ='/html/body/div[2]/main/cach/div[3]/div[32]/div[3]/div[2]/div/img'
button_ex32 = driver.find_element('xpath',ex32_b_xpath)
button_ex32.click()
time.sleep(2)
ex33_c_xpath ='/html/body/div[2]/main/cach/div[3]/div[33]/div[3]/div[3]/div/img'
button_ex33 = driver.find_element('xpath',ex33_c_xpath)
button_ex33.click()
time.sleep(2)
ex34_d_xpath ='/html/body/div[2]/main/cach/div[3]/div[34]/div[3]/div[4]/div/img'
button_ex34 = driver.find_element('xpath',ex34_d_xpath)
button_ex34.click()
time.sleep(2)
ex35_e_xpath ='/html/body/div[2]/main/cach/div[3]/div[35]/div[3]/div[5]/div/img'
button_ex35 = driver.find_element('xpath',ex35_e_xpath)
button_ex35.click()
