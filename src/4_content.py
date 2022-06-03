import requests
from pprint import pprint

response = requests.get('https://api.github.com')
print('response in bytes:\n\n', response.content)
print('\n\nresponse as text (unicode):\n\n', response.text)

# optional
response.encoding = 'utf-8'
print('\n\nresponse as text in UTF8:\n\n', response.text)
pprint(response.json())
print('\n\nresponse as json:\n\n', response.json())
