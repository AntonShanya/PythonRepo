import socket

c = socket.socket()

c.connect(("localhost",9999))

print("Write your name\n")
name=input()

c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())
