import requests

url = 'http://httpbin.org/cookies'
cookies1 = {'cookies_are':'working'}
rep = requests.get(url, cookies = cookies1)

print(rep.status_code)
print(rep.cookies)
print(rep.text)