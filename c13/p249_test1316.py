import PyPDF2

minutesFile = open('../resource/pdf/meetingminutes.pdf', 'rb')
reader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = reader.getPage(0)
waterReader = PyPDF2.PdfFileReader(open('../resource/pdf/watermark.pdf', 'rb'))

minutesFirstPage.mergePage(waterReader.getPage(0))
witer = PyPDF2.PdfFileWriter()
witer.addPage(minutesFirstPage)

for pageNum in range(1, reader.numPages):
    pageObj = reader.getPage(pageNum)
    witer.addPage(pageObj)

resultFile = open('../resource/pdf/output/watermarkedCover.pdf', 'wb')
witer.write(resultFile)
resultFile.close()
minutesFile.close()


print('Done')
