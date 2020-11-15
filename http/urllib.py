import gzip

if __name__ == '__main__':
    #
    url = 'http://ww.qq.com'

    response = urllib.request.urlopen(url)

    print(response.info()) # info response header info

    # print (response)
    b = response.read()

    # return status code
    print(response.status, response.code)

    # r.headers
    print(response.headers)

    print(response.headers.get('Content-Type'))

    data = gzip.decompress(b) # decompress data
    print(data.decode('GBK')) # return website data