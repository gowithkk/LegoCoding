
import socket
s = socket.socket(family='AF_INET', type='SOCK_STREM')

s.bind(('127.0.0.1', 6666))

s.listen(5)
print("I'm listening")