import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#want client to connect to server
s.connect((socket.gethostname(),1024))
msg=s.recv(1024)
print(msg.decode("utf-8"))
