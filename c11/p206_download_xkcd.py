#! python3
# Downloads every single XKCD comic.

import os

import bs4
import requests

url = 'http://xkcd.com'
# 代理
proxyDict = {'https': 'http://0.0.0.0:1087'}
# 设定主文件夹
os.chdir('/Users/moqi/Downloads/')
os.makedirs('xkcd', exist_ok=True)
# 设定最多下载十个，可以检验程序结果即可
count = 10

while not url.endswith('#') and count:
    print('Downloading page %s...' % url)
    res = requests.get(url, proxies=proxyDict)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='lxml')
    comicElem = soup.select('#comic img')

    if comicElem:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl, proxies=proxyDict)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    count -= 1

print('Done')

"""
Downloading page http://xkcd.com...
Downloading image http://imgs.xkcd.com/comics/scenario_4.png...
Downloading page http://xkcd.com/2288/...
Downloading image http://imgs.xkcd.com/comics/collectors_edition.png...
Downloading page http://xkcd.com/2287/...
Downloading image http://imgs.xkcd.com/comics/pathogen_resistance.png...
Downloading page http://xkcd.com/2286/...
Downloading image http://imgs.xkcd.com/comics/6_foot_zone.png...
Downloading page http://xkcd.com/2285/...
Downloading image http://imgs.xkcd.com/comics/recurring_nightmare.png...
Downloading page http://xkcd.com/2284/...
Downloading image http://imgs.xkcd.com/comics/sabotage.png...
Downloading page http://xkcd.com/2283/...
Downloading image http://imgs.xkcd.com/comics/exa_exabyte.png...
Downloading page http://xkcd.com/2282/...
Downloading image http://imgs.xkcd.com/comics/coronavirus_worries.png...
Downloading page http://xkcd.com/2281/...
Downloading image http://imgs.xkcd.com/comics/coronavirus_research.png...
Downloading page http://xkcd.com/2280/...
Downloading image http://imgs.xkcd.com/comics/2010_and_2020.png...
Done
"""
