import urllib.request
import urllib.parse

# request for header
req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://wwww.python.org/')
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: .  .  .)') # to imitate broswer
r = urllib.request.urlopen(req)

# return data using GET
params = urllib.parse.urlencode({'spam':1 ,'eggs':2 , 'bacon':0})
url = "http://httpbin.org/get?{}".format(params)
# url = "http://httpbin.org/get?%s" % params
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))

#
# # return data using POST
# data = urllib.parse.urlencode({'spam':1 ,'eggs':2 , 'bacon':0})
# data = data.encode('ascii')
# with urllib.request.urlopen("http://requestb.in/xrb182xr", data) as f:
#     print(f.read().decode('utf-8'))
