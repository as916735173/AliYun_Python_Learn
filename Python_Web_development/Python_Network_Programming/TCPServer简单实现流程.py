import socket
server = socket.socket()
print(server)
ipaddr = ('127.0.0.1', 9999)
server.listen()
s, raddr = server.accept()  # 等待对方连接过来
while True:
    data = s.recv(1024)
    print(data)
    s.send('ack.{}'.format(data.decode()).encode())

s.close()
print(server.bind(ipaddr))
server.close()