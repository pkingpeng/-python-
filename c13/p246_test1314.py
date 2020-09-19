import PyPDF2

pdf1Reader = PyPDF2.PdfFileReader(open('../resource/pdf/meetingminutes.pdf', 'rb'))
pdf2Reader = PyPDF2.PdfFileReader(open('../resource/pdf/meetingminutes2.pdf', 'rb'))

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


pdfOutputFile = open('../resource/pdf/combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

print('Done')
