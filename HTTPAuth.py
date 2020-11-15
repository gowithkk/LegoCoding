import requests
from requests.auth import HTTPBasicAuth

url = 'http://httpbin.org/basic-auth/liyi/123456'
rep = requests.get(url, auth = HTTPBasicAuth('liyi', '123456'))

# return status code
print(rep.status_code)