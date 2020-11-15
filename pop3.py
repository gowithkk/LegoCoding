import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = 'xx@gmail.com'
password = 'xxxxx'
pop3_server = 'pop.gmail.com'

# connect to server
server = poplib.POP3(pop3_server)

# authentication
server.user(email)
server.pass_(password)

# stat() returns number of emails and size
# %s is string; %d is integer
# server.stats() will return two values: number and size
print('Messages: %s. Size: %s' % server.stat())

# list() returns sequence of emails
resp, mails, octets = server.list()
