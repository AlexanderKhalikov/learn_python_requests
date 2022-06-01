import requests

response = requests.get('https://api.github.com')
print('response headers:\n\n', response.headers)

# .headers returns a dictionary-like object, allowing you to access header values by key.
# For example, to see the content type of the response payload, you can access Content-Type:

print('\n\ncertain header by key:\n\n', response.headers['Content-Type'])
