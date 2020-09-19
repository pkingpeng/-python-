#! python3
# Opens several Google search results.

import webbrowser

import bs4
import requests

proxyDict = {'https': 'http://0.0.0.0:1087'}

print('Googling...')
# url = 'https://www.google.com/search?q=%s' % ('%20'.join(sys.argv[1:]))

# test url
url = 'https://www.google.com/search?q=something'
res = requests.get(url, proxies=proxyDict)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='lxml')

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('https://www.google.com%s' % (linkElems[i].get('href')))

"""
没成功，因为 soup.select('.r a') 没有匹配到，后面再研究
"""
