def print_pinnic(item_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))

    for k, v in item_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))


picnic = {'sandwoches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_pinnic(picnic, 12, 5)
print('-' * 30)
print_pinnic(picnic, 20, 6)
