import bs4

exampleHtml = open('../resource/html/example.html')
exampleSoup = bs4.BeautifulSoup(exampleHtml.read(), features='lxml')

elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

print('-' * 50)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(pElems[1])
print(pElems[1].getText())
print(pElems[2])
print(pElems[2].getText())

"""
<class 'bs4.element.ResultSet'>
1
<class 'bs4.element.Tag'>
Al Sweigart
<span id="author">Al Sweigart</span>
{'id': 'author'}
--------------------------------------------------
<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>
Download my Python book from my website.
<p class="slogan">Learn Python the easy way!</p>
Learn Python the easy way!
<p>By <span id="author">Al Sweigart</span></p>
By Al Sweigart
"""
