import PyPDF2

pdfFileObj = open('../resource/pdf/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
text1 = pageObj.extractText()
print(text1)

"""
19
OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of 
March 7
, 2014
        
     The Board of Elementary and Secondary Education shall provide leadership and 
create policies for education that expand opportunities for children, empower 
families and communities, and advance Louisiana in an increasingly 
competitive glob
al market.
 BOARD 
 of ELEMENTARY
 and 
 SECONDARY
 EDUCATION  
"""
