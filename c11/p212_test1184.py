from selenium import webdriver
"""
Google 对登陆界面进行了保护，id 是乱码，没有规律。
不过测试自动填写已经成功了，虽然只是输入了一个邮箱名称。
"""
browser = webdriver.Firefox()

browser.get('https://www.gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('not_my_real_email@gmail.com')
# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('12345')
# passwordElem.submit()
