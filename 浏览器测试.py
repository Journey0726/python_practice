from selenium import webdriver
from time import sleep
browser = webdriver.Chrome(executable_path='D:\PYthon\chromedriver.exe')
browser.get('https://qzone.qq.com/')
browser.switch_to.frame('login_frame')
a=browser.find_element_by_id("switcher_plogin")
a.click()
userName = browser.find_element_by_id('u')
passward = browser.find_element_by_id('p')
userName.send_keys('1549120948')
passward.send_keys('2257352356hh')
butten = browser.find_element_by_id('login_button')
butten.click()