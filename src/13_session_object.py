import requests
from getpass import getpass
import json
from pprint import pprint as pp

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# You can inspect the response just like you did before
pp(json.dumps(dict(response.headers)))
print('\n')
pp(json.dumps(response.json()))

