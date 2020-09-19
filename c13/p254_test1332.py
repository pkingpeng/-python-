import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []

    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)

    return '\n'.join(fullText)


print(getText('../resource/word/demo.docx'))

"""
Document Title
A plain paragraph with some bold and some italic
Heading, level 1
Intense quote
first item in unordered list
first item in ordered list
"""
