import json

from twilio.rest import Client

dic = json.loads(open('/Users/moqi/Documents/Doc/twilio.json').read())
sid = dic['sid']
token = dic['token']

twilioCli = Client(sid, token)
message = twilioCli.messages.create(body='Just test message', from_=dic['from'], to=dic['to'])
print(message.sid)
print('It works, all done.')
