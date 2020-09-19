import json

from twilio.rest import Client

from c15.p292_multidownload_xkcd import downloadXkcd

dic = json.loads(open('/Users/moqi/Documents/Doc/twilio.json').read())
sid = dic['sid']
token = dic['token']

twilioCli = Client(sid, token)

downloadXkcd(0, 10)
test_message = 'xkcd 网站前 10 个漫画已经下载完毕了。😄😄😄😄😄😄😄😄😄😄'

message = twilioCli.messages.create(body=test_message, from_=dic['from'], to=dic['to'])
print(message.sid)
print('It works, all done.')
