import socket

host = "192.168.0.103"
port_windows = 7899

while True:
    try:
        socket_windows = socket.socket()
        socket_windows.connect((host, port_windows))
        temp = socket_windows.recv(1024).decode()
        if temp:
            print(temp)
            continue

    except Exception:
        continue
