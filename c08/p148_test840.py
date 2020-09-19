import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
file_obj = open('../gererate_python_file/my_cat.py', 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')
file_obj.close()

