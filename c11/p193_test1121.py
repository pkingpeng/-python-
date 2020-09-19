import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

"""
<class 'requests.models.Response'>
True
179378
﻿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare


*******************************************************************
THIS EBOOK WAS ONE OF PROJECT GUTENBERG'S EARLY FILES PRODUCED AT A
TIME WHEN PROOFING METHODS AND TOO
"""
