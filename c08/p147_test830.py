import shelve

shhelf_file = shelve.open('../resource/binary/my_binary_data')
cats = ['Zophie', 'Pooka', 'Simon']
shhelf_file['cats'] = cats
shhelf_file.close()

shhelf_file = shelve.open('../resource/binary/my_binary_data')
print(type(shhelf_file))
print(shhelf_file['cats'])
shhelf_file.close()

shhelf_file = shelve.open('../resource/binary/my_binary_data')
print(list(shhelf_file.keys()))
print(list(shhelf_file.values()))
shhelf_file.close()
