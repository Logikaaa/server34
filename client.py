import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
name = input("Введи Ім'я:")
client_socket.send(name.encode())
print(client_socket.recv(1024).decode())

command = input("Введи команду (NAME/EXIT):")
client_socket.send(command.encode())
print(client_socket.recv(1024).decode())


client_socket.close()