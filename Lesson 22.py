#Selenium WebDriver
# https://selenium-python.readthedocs.io/api.html
# https://www.geeksforgeeks.org/web-driver-methods-in-selenium-python/



# for mac
# EXE_PATH = r'path\to\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
# driver = webdriver.Chrome(executable_path=EXE_PATH)
# driver.get('https://google.com')
import os
import time
from selenium import webdriver

# driver_path_chrome = os.getcwd() + '\chromedriver.exe'
driver_path_firefox = os.getcwd() + '\geckodriver.exe'
# driver_path_edge = os.getcwd() + '\msedgedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path_chrome)

# driver = webdriver.Edge(executable_path=driver_path_edge)

driver = webdriver.Firefox(executable_path=driver_path_firefox)
driver.maximize_window() # Максимизирует
# driver.set_window_size(300.100) #- размер окна
driver.get('https://chromedriver.chromium.org/downloads')
driver.get_screenshot_as_file('downloads1.png')
time.sleep(5)
driver.get('https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.102/')
driver.get_screenshot_as_file('downloads2.png')
time.sleep(5)
driver.get('https://github.com/mozilla/geckodriver/releases')
driver.get_screenshot_as_file('downloads3.png')
time.sleep(5)
driver.quit()
#dribr.close()


