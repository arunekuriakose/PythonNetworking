import socket
#CREATE SOCKET

'''AF_INET=(address family-address from internet-requires a pair of host and port number
   host can be url of particular website or its address and the port number is an integer)'''
'''SOCK_STREAM = Used to create TCP protocols'''

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

'''
bind method is used to bind to the client
Bind method accepts two parameters: a host and a port number  (host,portnumber)
gethostname() - used when client and server are on the same system
portnumber>1023 - non previlaged number
'''
s.bind((socket.gethostname(),1024))


s.listen(5)
#Wwhile connection is True
while True:
    #want server to accept client socket and its address
    clt,adr=s.accept()
    #fstring - basically a literal string prefixed with an f and contains python expressions within braces{}.
    print(f'Connection to {adr} established')
    #Pass message from server to client
    #bytes - utf-8
    clt.send(bytes("Socket Programming in Python","utf-8"))