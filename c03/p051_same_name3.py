def spam():
    global eggs
    eggs = 'spam'


def bacon():
    eggs = 'bacon'


def ham():
    print(eggs)


eggs = 12
spam()
print(eggs)

"""
spam
"""
