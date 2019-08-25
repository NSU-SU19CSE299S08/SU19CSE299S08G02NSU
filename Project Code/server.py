from socket import *

host = "192.168.43.115"
port_android = 7890

while True:
    socket_android = socket(AF_INET, SOCK_STREAM)
    socket_android.bind((host, port_android))
    socket_android.listen(5)
    c_android, addr_android = socket_android.accept()
    temp = (c_android.recv(1024).decode('utf-8'))
    if temp:
        print(temp)
        socket_android.close()