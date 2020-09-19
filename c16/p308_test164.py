import json

import imapclient
# 参考这个链接 https://stackoverflow.com/a/43733889 安装 pip install pyzmail36
import pyzmail
import pprint

dic = json.loads(open('/Users/moqi/Documents/Doc/qq_imap_stmp_test.json').read())

imapObj = imapclient.IMAPClient('imap.qq.com', 993, ssl=True)
# 授权码
print(imapObj.login(dic['from'] + '@qq.com', 'glruysrasauwbegg'))
print(imapObj.welcome)

print('\n', '-' * 50, '\n')

pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])
print(UIDs)

rawMessage = imapObj.fetch([330], [b'BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessage[330][b'BODY[]'])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('tp'))
print(message.get_address('cc'))
print(message.get_address('bcc'))

print('\n', '-' * 50, '\n')

pprint.pprint(message.text_part)
pprint.pprint(message.text_part.get_payload().decode(message.text_part.charset))
imapObj.logout()

print('All Done.')

"""
b'Success login ok'
b'* OK [CAPABILITY IMAP4 IMAP4rev1 ID AUTH=LOGIN NAMESPACE] QQMail XMIMAP4Server ready'

 -------------------------------------------------- 

[((b'\\NoSelect', b'\\HasChildren'), b'/', '其他文件夹'),
 ((b'\\HasNoChildren',), b'/', 'INBOX'),
 ((b'\\HasNoChildren',), b'/', 'Sent Messages'),
 ((b'\\HasNoChildren',), b'/', 'Drafts'),
 ((b'\\HasNoChildren',), b'/', 'Deleted Messages'),
 ((b'\\HasNoChildren',), b'/', 'Junk'),
 ((b'\\HasNoChildren',), b'/', '其他文件夹/QQ邮件订阅'),
 ((b'\\HasNoChildren',), b'/', '被感染项目')]

[328, 329, 330]
Re: Hello Tom Smith
('********************', '********************')
('', '')
('', '')
('', '')

 -------------------------------------------------- 

MailPart<*text/plain charset=utf-8 len=182>
('777\r\n'
 '\r\n'
 '\r\n'
 '444\r\n'
 '\r\n'
 '\r\n'
 '8\r\n'
 '\r\n'
 '\r\n'
 '\r\n'
 '\r\n'
 '5555\r\n'
 '\r\n'
 '发自我的iPhone\r\n'
 '\r\n'
 '\r\n'
 '------------------ Original ------------------\r\n'
 'From:  <&gt;\r\n'
 'Date: Sun,Apr 12,2020 7:25 PM\r\n'
 'Subject: Re: Hello Tom Smith')
All Done.
"""
