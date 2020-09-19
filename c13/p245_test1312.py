import PyPDF2
from PyPDF2.utils import PdfReadError

reader = PyPDF2.PdfFileReader(open('../resource/pdf/encrypted.pdf', 'rb'))
print('isEncrypted: %s' % reader.isEncrypted)

try:
    reader.getPage(0)
except PdfReadError as error:
    print(error)

decrypt = reader.decrypt('rosebud')
print(decrypt)

# 上一步返回解密成功，但是依然无法打开文件
print('again isEncrypted: %s' % reader.isEncrypted)

"""
isEncrypted: True
file has not been decrypted
1
again isEncrypted: True
"""
