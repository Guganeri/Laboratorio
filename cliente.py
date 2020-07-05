import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 8291

s.connect((host, port))
data = s.recv(1024)
print(data.decode('ascii'))