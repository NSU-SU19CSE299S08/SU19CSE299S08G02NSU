from socket import *
import os

host = "127.0.0.1"
port = 9999
s = socket(AF_INET, SOCK_STREAM)

s.bind(host, port)
s.listen(5)
while True:
    c, addr = s.accept()
    print(c.recv(1024).decode('utf-8'))
