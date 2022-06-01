import requests

print(requests.post('https://httpbin.org/post', data={'key':'value'}))
print(requests.put('https://httpbin.org/put', data={'key':'value'}))
print(requests.delete('https://httpbin.org/delete'))
print(requests.head('https://httpbin.org/get'))
print(requests.patch('https://httpbin.org/patch', data={'key':'value'}))
print(requests.options('https://httpbin.org/get'))

# Each function call makes a request to the httpbin service using the corresponding HTTP method.
# For each method, you can inspect their responses in the same way you did before:

response = requests.head('https://httpbin.org/get')
print(response.headers['Content-Type'])


response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])
