# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #создаёт объект сокета
    s.connect((HOST, PORT)) #для подключения к серверу
    s.sendall(b"Hello, world") #для отправки сообщения
    data = s.recv(1024) #для чтения ответа сервера

print(f"Received {data!r}")
