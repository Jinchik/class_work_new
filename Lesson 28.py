from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get('https://www.yanigen.com.ua')
driver.maximize_window()
time.sleep(5)
driver.get_screenshot_as_file('google.png')

home_ru = '//a[contains(text(),"ГЛАВНАЯ")]'
home_ru2 = '//a[contains(text(),"ГОЛОВНА")]'
home_ru3 = '//a[contains(text(),"HOME")]'


home2_ru = "//ul[@class='menumain']/li/a[@href='/ru/']"
a = '//a[@class="link_img"][@href="/ru/shop/documentsholders/heirloom3-detail"]/img[@class="bigimg"]'
b = '//img[@class="bigimg"][@src="/images/stories/virtuemart/product/compact_07.png"]'
c = '//a[@href="#"][@data-direction="forward"]'

#//div[contains(@class,'gkPrice') ][contains(@class,'custom_price')]
button = driver.find_element('xpath', b)
button.click()
time.sleep(5)
button2 = driver.find_element('xpath', c)
button2.click()