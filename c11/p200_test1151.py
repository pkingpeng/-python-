import bs4
import requests

res = requests.get('https://www.github.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, features='lxml')
print(type(noStarchSoup))

exampleHtml = open('../resource/html/example.html')
exampleSoup = bs4.BeautifulSoup(exampleHtml, features='lxml')
print(type(exampleSoup))

"""
<class 'bs4.BeautifulSoup'>
<class 'bs4.BeautifulSoup'>
"""
