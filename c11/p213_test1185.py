from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
测试窗口滑动 -> 成功
"""
browser = webdriver.Firefox()

browser.get('https://www.v2ex.com/?tab=hot')
htmlElem = browser.find_element_by_tag_name('html')

for i in range(5):
    sleep(1)
    htmlElem.send_keys(Keys.PAGE_DOWN)

for i in range(5):
    sleep(1)
    htmlElem.send_keys(Keys.PAGE_UP)
