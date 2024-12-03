import socket

PORT = 12345
HOST = "localhost"

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((HOST, PORT))

pie = input("¿Cuánto calzas? ")
clienteSocket.sendall(pie.encode())

while True:
    mensaje = clienteSocket.recv(1024).decode()
    print(mensaje) 

    if "Da un paso" in mensaje:
        respuesta = input("> ")
        clienteSocket.send(respuesta.encode())

    if "¡Ganaste!" in mensaje:
        print("¡Felicidades, ganaste!")
        break


clienteSocket.close()
