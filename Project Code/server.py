from socket import *

host = "192.168.0.103"
port_android = 7890
port_windows = 7899

while True:
    socket_android = socket(AF_INET, SOCK_STREAM)
    socket_android.bind((host, port_android))
    socket_android.listen(5)
    c_android, addr_android = socket_android.accept()
    temp = (c_android.recv(1024).decode('utf-8'))
    if temp:
        print(temp)
        socket_android.close()
        socket_windows = socket(AF_INET, SOCK_STREAM)
        socket_windows.bind((host, port_windows))
        socket_windows.listen(5)
        c_windows, addr_windows = socket_windows.accept()
        c_windows.send(temp.encode())
        c_windows.close()

# while True:
#     socket_android = socket(AF_INET, SOCK_STREAM)
#     socket_android.bind((host, port_android))
#     socket_android.listen(5)
#     while True:
#         c_android, addr_android = socket_android.accept()
#         temp = (c_android.recv(1024).decode('utf-8'))
#         if temp:
#             socket_android.close()
#             break
#     socket_windows = socket(AF_INET, SOCK_STREAM)
#     socket_windows.bind((host, port_windows))
#     socket_windows.listen(5)
#     c_windows, addr_windows = socket_windows.accept()
#     c_windows.send(temp.encode())
#     c_windows.close()
