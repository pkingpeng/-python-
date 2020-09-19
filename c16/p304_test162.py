import json
import smtplib

"""
QQ 邮箱的 SMTP/IMAP 帮助信息参考：https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=331
"""

dic = json.loads(open('/Users/moqi/Documents/Doc/qq_imap_stmp_test.json').read())
smtpObj = smtplib.SMTP('smtp.qq.com', 587)
print(smtpObj.ehlo())
print(smtpObj.starttls())

print(smtpObj.login(dic['from'] + '@qq.com', 'glruysrasauwbegg'))

msg = 'Subject: Hello Tom Smith'
smtpObj.sendmail(dic['from'] + '@qq.com', dic['to'] + '@qq.com', msg)
print('Everything Done.')
smtpObj.quit()

"""
(250, b'newxmesmtplogicsvrszc5.qq.com\nPIPELINING\nSIZE 73400320\nSTARTTLS\nAUTH LOGIN PLAIN\nAUTH=LOGIN\nMAILCOMPRESS\n8BITMIME')
(220, b'Ready to start TLS from 111.197.60.45 to newxmesmtplogicsvrszc5.qq.com.')
(235, b'Authentication successful')
Everything Done.
"""
