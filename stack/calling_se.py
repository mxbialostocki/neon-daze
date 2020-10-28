import requests

res = requests.get('https://mxbialostocki.github.io/')

if res:
  print('Recieved response OK: ', res.status_code)
else:
  print('Response failed')
