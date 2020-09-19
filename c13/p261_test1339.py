import docx
from docx.shared import Inches, Cm

doc = docx.Document()

doc.add_picture('../resource/image/zophie.png', width=Inches(5), height=Cm(20))

doc.save('../resource/word/output/imageTest.docx')
print('Done')
