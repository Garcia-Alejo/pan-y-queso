import socket

PORT = 12345
HOST = "localhost"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(2)
print(f"Servidor escuchando en {HOST}:{PORT}")

conexion, direccion = serverSocket.accept()
print(f"Jugador conectado desde {direccion}")


pie = conexion.recv(1024).decode()
print(f"El cliente calza: {pie}")

tamaño = 100

while True:
    print(f"pititoss")
    paso = conexion.recv(1024).decode()

    if paso:
        tamaño -= pie
        print(f"El cliente ha enviado: {paso}. Contador: {tamaño}")

        if tamaño <= 0:
            conexion.sendall("¡Ganaste!\n".encode())
            print("El cliente ha ganado")
            break
        else:
            conexion.sendall(f"Da otro paso. Contador restante: {tamaño}\n".encode())

 
conexion.close()
serverSocket.close()
