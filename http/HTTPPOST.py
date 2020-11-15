import requests

url = 'http://httpbin.org/post'
data = {'key1':'value1', 'key2':'value2'}

r = requests.post(url, data = data)

print(r.text)

# other HTTP methods

r = requests.put('http://httpbin.org/put', data = data)
r = requests.delte('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

