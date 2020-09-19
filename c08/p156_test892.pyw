import re

file = open('../resource/txt/anav.txt')
context = file.read()
all_pattern_words = 'ADJECTIVE|NOUN|ADVERB|VERB'

pattern = re.compile(all_pattern_words)

while True:
    matches = pattern.search(context)

    # 如果 matches 为 None 表示已经没有匹配到的词了
    if not matches:
        print('\nAll match words was replaced, It is done.\n')
        break

    data = matches.group()
    input1 = input('Enter an ' + data + ' :')
    # 每次只替换一个值，不替换所有
    context = re.sub(data, input1, context, 1)

print(context)

new_file = open('../resource/txt/anav_new.txt', 'w')
new_file.write(context)
new_file.close()
