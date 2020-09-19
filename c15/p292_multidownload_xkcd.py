#! python3
# Downloads XKCD comiccs using multiple threads.

import os
import threading

import bs4
import requests


def downloadXkcd(startComic, endComic):
    os.chdir('/Users/moqi/Downloads')
    xkcd_dir = 'multidownload_xkcd'
    os.makedirs(xkcd_dir, exist_ok=True)
    for urlNumber in range(startComic, endComic):

        # 跳过 0 和 404 页面
        if urlNumber in [0, 404]:
            continue

        fullUrl = 'https://xkcd.com/%s' % urlNumber
        print('Downloading page %s...\n' % fullUrl)
        res = requests.get(fullUrl)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='lxml')

        comicElem = soup.select('#comic img')
        # 判断数组不为空
        if not comicElem:
            print('Could not find comic image')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            print('Downloading image %s...' % comicUrl)
            comicRes = requests.get(comicUrl)
            comicRes.raise_for_status()

            imageFile = open(os.path.join(xkcd_dir, os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# 放在 main 方法里本地测试，否则外部调用会执行代码
if __name__ == '__main__':
    # 单线程调试，方便解决问题
    # downloadXkcd(1, 10)

    # 多线程运行，更充分利用 CPU 和带宽
    downloadThreads = []
    for i in range(0, 1400, 100):
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    for downloadThread in downloadThreads:
        downloadThread.join()

    print('All Done.')
