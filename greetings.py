import base64

def greetings_pubsub(data, context):
  if 'data' in data:
    name = base64.b64decode(data['data']).decode('utf-8')
  else:
    name = 'folks'
  print(data)
  print('Greetings {} from Linux Academy!'.format(name))
