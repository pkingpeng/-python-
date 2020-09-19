import PyPDF2

minutesFile = open('../resource/pdf/meetingminutes.pdf', 'rb')
reader = PyPDF2.PdfFileReader(minutesFile)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader.numPages):
    writer.addPage(reader.getPage(pageNum))

writer.encrypt('test')
resultPdf = open('../resource/pdf/output/encyptedMinutes.pdf', 'wb')
writer.write(resultPdf)
resultPdf.close()
minutesFile.close()

print('Done')
