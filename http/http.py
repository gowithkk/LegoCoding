import SimpleHTTPServer

port = 80

httpd= SimpleHTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

