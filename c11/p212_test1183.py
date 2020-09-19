from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))

browser.get('https://inventwithpython.com')

try:
    link_elem = browser.find_element_by_id('navbarDropdownReadMenuLink')
    print(type(link_elem))

    link_elem.click()
    print('Found <%s> element with that class name! ' % link_elem.tag_name)
except:
    print('Was not able to find an element with that name.')

"""
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
<class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
Found <a> element with that class name! 
"""
