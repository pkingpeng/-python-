from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))

browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('nav-item')
    print('Found <%s> element with that class name! ' % elem.tag_name)
except:
    print('Was not able to find an element with that name.')
