import docx

doc = docx.Document()
doc.add_paragraph('Hello Tom Smith')

doc.save('../resource/word/output/helloworld.docx')
print('Done')
