import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# By passing the dictionary {'q': 'requests+language:python'} to the params parameter of .get(),
# you are able to modify the results that come back from the Search API.
# You can pass params to get() in the form of a dictionary, as you have just done, or as a list of tuples:

print(requests.get('https://api.github.com/search/repositories',
                   params=[('q', 'requests+language:python')], )
      )
