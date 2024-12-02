import socket

PORT = 12345
HOST = "localhost"

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((HOST, PORT))

pie = input("¿Cuánto calzas? ")
clienteSocket.send(pie.encode())

while True:
	print(f"pitito")
    mensaje = clienteSocket.recv(1024).decode()
    print(mensaje) 

    if "da un paso" in mensaje:
        respuesta = input("> ")
        clienteSocket.send(respuesta.encode())

    if "¡Ganaste!" in mensaje:
        print("¡Felicidades, ganaste!")
        break


clienteSocket.close()
