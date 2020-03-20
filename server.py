import socket

s = socket.socket() #default IPV4+TCP
print('Socket created')

s.bind(('localhost',9999))

s.listen(3)
print("Waiting for connection")

while True:
    c,addr = s.accept() #c=>socket del client, addr=>indirizzo client
    name = c.recv(1024).decode()
    print("{} , {}".format(addr,name))

    c.send(bytes("Welcome to Client-Server App TLSK","utf-8"))
    c.close()


