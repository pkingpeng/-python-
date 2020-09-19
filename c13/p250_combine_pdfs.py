#! python3
# Combines all the PDFs in the current working directory into a single PDF.

import os

import PyPDF2

# 切换 os 目录到本项目 pdf 目录下
os.chdir('../resource/pdf')

pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort()

writer = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    reader = PyPDF2.PdfFileReader(open(filename, 'rb'))

    # 跳过加密的 pdf
    if reader.isEncrypted:
        continue

    # 跳过所有 pdf 的第一页
    for pageNum in range(1, reader.numPages):
        writer.addPage(reader.getPage(pageNum))

# 目录已经定位到本项目 pdf，所以只需要名称
pdfOutput = open('all.pdf', 'wb')
writer.write(pdfOutput)
pdfOutput.close()

print('Done')
