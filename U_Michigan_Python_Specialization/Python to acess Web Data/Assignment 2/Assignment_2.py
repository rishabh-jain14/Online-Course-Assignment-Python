import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
inst = 'GET http://data.pr4e.org/intro-short.txt HTTP/2.0\r\n\r\n'.encode()
mysock.send(inst)

while True:
    data = mysock.recv(1024)
    if len(data) < 1 :
        break
    print(data.decode())

mysock.close()