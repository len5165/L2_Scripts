# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # используется для привязки сокета к определённому сетевому интерфейсу и номеру порта
    s.listen()  # Он определяет количество непринятых подключений, которые система допустит, прежде чем отклонить новые подключения
    print("Server listen")
    conn, addr = s.accept()  # Метод блокирует выполнение и ожидает входящего соединения. Когда клиент подключается, он возвращает новый объект сокета, представляющий соединение, и кортеж, содержащий адрес клиента
    with conn:  # Оператор with используется с conn для автоматического закрытия сокета в конце блока
        # print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  # для перебора блокирующих вызовов
            if not data:
                break
            conn.sendall(data)  # отправлять данные обратно
            print(data)
