#!/usr/local/bin/python3

table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(data):
    col_widths = [0] * len(data)

    for i in range(len(data)):
        for e in data[i]:
            col_widths[i] = max(col_widths[i], len(e))

    print(
        data[0][0].rjust(col_widths[0]) + ' ' + data[1][0].ljust(col_widths[1]) + ' ' + data[2][0].ljust(col_widths[2]))
    print(
        data[0][1].rjust(col_widths[0]) + ' ' + data[1][1].ljust(col_widths[1]) + ' ' + data[2][1].ljust(col_widths[2]))
    print(
        data[0][2].rjust(col_widths[0]) + ' ' + data[1][2].ljust(col_widths[1]) + ' ' + data[2][2].ljust(col_widths[2]))
    print(
        data[0][3].rjust(col_widths[0]) + ' ' + data[1][3].ljust(col_widths[1]) + ' ' + data[2][3].ljust(col_widths[2]))


print_table(table_data)
