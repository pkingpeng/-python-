import openpyxl
# 看是否能根据坐标突破 26 个字母表的 column 限制
# from openpyxl.utils import get_column_letter

# 将这个数字改为 input 应付 26 个字母的乘法表
num = 10

wb = openpyxl.Workbook()
sheet = wb.active

az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(1, num + 1):
    sheet['A' + str(i + 1)] = i
    sheet[az[i] + '1'] = i

for i in range(2, num + 2):
    for j in range(2, num + 2):
        index = az[i - 1] + str(j)
        sheet[index] = (i - 1) * (j - 1)


wb.save('../resource/excel/output/multiplicationTable.xlsx')
print('Done')
