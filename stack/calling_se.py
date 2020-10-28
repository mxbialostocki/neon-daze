import requests
import json 

# deconstruct the api request parameters
API_URL = 'https://api.stackexchange.com/'
API_VERSION = '2.2/'
API_MODIFIER = 'questions?'
# 1 September 2020, 00:00:00 // 30 September 2020, 23:59:59
from_date = '1598918400'
to_date = '1601510399'
DEFAULT_SORT = '&order=desc&sort=activity'
tagged = 'python'
site = 'stackoverflow'

# write the parameters into a string
stack_exchange_string = '{API_URL}{API_VERSION}{API_MODIFIER}fromdate={from_date}&todate={to_date}{DEFAULT_SORT}&tagged={tagged}&site={site}'

# format the string to make the request
stack_exchange_request = stack_exchange_string.format(
  API_URL=API_URL,
  API_VERSION=API_VERSION,
  API_MODIFIER=API_MODIFIER,
  from_date=from_date,
  to_date=to_date,
  DEFAULT_SORT=DEFAULT_SORT,
  tagged=tagged,
  site=site
  )
print(stack_exchange_request)

# call a GET request to the api using the formatted string
response = requests.get(stack_exchange_request)

# check if the response was sucessful, or notify of error
if response:
  print('Request is successful: ', response.status_code)
else:
  print('Request returned an error.')

headers = response.headers
text = response.text

# create a json object from the response
data_response = response.json()

# and write the json object to a new file
with open('./data/items.json', 'w') as json_file:
  json.dump(data_response, json_file)
  
json_file.close()