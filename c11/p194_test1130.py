import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try:
    res.raise_for_status()
except Exception as error:
    print('These was a problem: %s.' % error)

playFile = open('../resource/txt/RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
