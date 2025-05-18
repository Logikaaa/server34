import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))

server_socket.listen(1)
connection, address = server_socket.accept()
client_name = connection.recv(1024).decode()
connection.send(f"Вітаю {client_name} на сервері." .encode())

command = connection.recv(1024).decode()
if command == "NAME":
    connection.send(f"Твоє ім'я: {client_name}".encode)
elif command == "EXIT":
    connection.send(f"Бувай: {client_name}".encode)
    connection.close()
else:
    connection.send(f"Такої команди не існує: {client_name}".encode)

server_socket.close()