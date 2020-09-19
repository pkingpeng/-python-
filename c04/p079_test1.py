from typing import List


def hanble_list(str_list: List[str]) -> str:
    length = len(str_list)
    if not str_list:
        return ''
    elif length == 1:
        return str_list[0]
    else:
        res = '\''

        for i in range(length):
            if i < length - 1:
                res += (str_list[i] + ', ')
            else:
                res += ('and ' + str_list[length - 1] + '\'')

        return res


if __name__ == '__main__':
    spam = ['apple', 'bananas', 'tofu', 'cats']
    print(hanble_list(spam))

    spam = ['a', 'b', 'c', 'd']
    print(hanble_list(spam))
