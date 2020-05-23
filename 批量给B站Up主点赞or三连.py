from time import sleep
from selenium import webdriver
driver=webdriver.Chrome('F:\\作弊!!!\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://space.bilibili.com/390461123')
driver.find_elements_by_xpath('//h3[@class="section-title"]/a[1]')[0].click()
for li in driver.find_elements_by_xpath('//ul[@class="clearfix cube-list"]/li/a[2]'):
    print(li.text)