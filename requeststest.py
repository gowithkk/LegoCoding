import requests
import time

# define URL
url = 'http://httpbin.org/get'

# GET a website
response = requests.get(url)

# print returned data using text and content
# print(response)
# print(response.text)
# print(response.content)

# Get a website with headers
headers = {'user-agent':'my-app/0.0.1'}
r = requests.get(url, headers = headers)
print(r)

# GET HTTP status code and reason
print(r.status_code, r.reason)
# get response dat
print(r.text)
# get response headers
print(r.headers)
# get in json
print(r.json())

# get specific header values
print(r.headers)
print(r.headers.get('Content-Type'))
print(r.headers['Content-Length'])

# get cookies
print(r.cookies)

