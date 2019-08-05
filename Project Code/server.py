from socket import *
import os

host = "103.25.120.190"
port = 9999
s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print(c.recv(1024).decode('utf-8'))
