import PyPDF2

reader = PyPDF2.PdfFileReader(open('../resource/pdf/meetingminutes.pdf', 'rb'))
page = reader.getPage(0)
page.rotateClockwise(90)

writer = PyPDF2.PdfFileWriter()
writer.addPage(page=page)

resultFile = open('../resource/pdf/output/rotatedPage.pdf', 'wb')
writer.write(resultFile)
resultFile.close()


print('Done')
