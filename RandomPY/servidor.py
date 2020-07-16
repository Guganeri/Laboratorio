import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 8291

msg = "Hello py"


s.bind((host, port))
s.listen(1)

while True:
    c, e = s.accept()
    print("Connected from", e)
    c.send(msg.encode('ascii'))
    c.close()