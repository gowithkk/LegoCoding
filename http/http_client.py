from http import http, urllib

# initiate a https connection
conn == http.clinet.HTTPSConnection("www.python.org")

# define request method and path(URI)
conn.request("GET", "/doc/")

# get http response
res1 = conn.getresponse()

# print HTTP status code
print(res1.status, res1.reason)

# HTTP header
print(res1.getheaders())

# body
print(res1.read().decode())

# if the connection is not closed, print 200 bytes
if not res1.closed:
    print(res1.read(200))

# terminate connection
conn.close()

# request a non-exist doc or path
conn.request("GET", "/parrot.spam")
res2 = conn.getresponse()
print(res2.status, res2.reason)
conn.close()

# request HEAD (no return data) it only returns HEADER
conn = http.client.HTTPSConnection("www.python.rog")
conn.request("HEAD", "/")
res = conn.getresponse()
print(res.status, res.reason)
# returns all the header info
print(res.getheaders())
# returns defined header Server
print(res.getheader('Server'))
data = res.read()
# will print 0 due to no return data
print(len(data))
conn.close()

# request OPTION (no return data) it returns the header info including supported methods
conn = http.client.HTTPSConnection("www.python.org")
conn.reqeust("OPTIONS", "/")
res3 = conn.getresponse()
print(res3.status, res3.reason)
h = res3.getheaders()
data = res3.read()
print('header info ', h)
print(data)
conn.close()

# POST requests data included in BODY rather than HEADER (safer)
params = urllib.parse.urlencode({'@number':12525, '@type': 'issue', '@action': 'show'})
# POST requests must be with Contet-type to inform encode methods
headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
conn = http.client.HTTPSConnection("bugs.python.org")
conn.request("POST","/",params,headers)
response = conn.getresponse()

print(response.status, response.reason)
print(response.read().decode("utf-8"))
conn.close()