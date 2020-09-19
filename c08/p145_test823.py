bacon = open('../resource/txt/bacon.txt', 'w')
bacon.write('Hello world!\n')
bacon.close()

bacon = open('../resource/txt/bacon.txt', 'a')
bacon.write('Hello Python3')
bacon.close()

bacon = open('../resource/txt/bacon.txt')
context = bacon.read()
bacon.close()

print(context)
