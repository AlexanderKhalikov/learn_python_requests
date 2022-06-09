import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
elif response.status_code == 503:
    print('вы ввели неверный пароль')

# requests goes one step further in simplifying this process for you.
# If you use a Response instance in a conditional expression, it will evaluate to True if the status code was between 200 and 400, and False otherwise.

# Therefore, you can simplify the last example by rewriting the if statement:

print(type(response))
if response:
    print('Success!')
else:
    print('An error has occurred.')
