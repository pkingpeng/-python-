"""
参考这个链接： https://stackoverflow.com/a/40208762
在这里下载了最新的 mac 的压缩包文件：https://github.com/mozilla/geckodriver/releases
然后将其配置在可执行的目录里，程序得以运行
"""
from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))

browser.get('https://www.google.com')
"""
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
"""
