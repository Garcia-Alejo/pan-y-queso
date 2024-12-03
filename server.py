import socket
import threading

PORT = 12345
HOST = "localhost"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(2)
print(f"Servidor escuchando en {HOST}:{PORT}")

tamaño = 100

clientes = []

def manejar_cliente(conexion, direccion, num_cliente):
    global tamaño

    pie = conexion.recv(1024).decode()
    print(f"El cliente {num_cliente} calza: {pie}")

    pie = int(pie)

    conexion.sendall(f"Jugador {num_cliente}, Da un paso. Contador restante: {tamaño}\n".encode())

    while True:
        paso = conexion.recv(1024).decode()

        if paso:
            tamaño -= pie
            print(f"El cliente {num_cliente} ha enviado a dado un paso. Contador restante: {tamaño}")

            if tamaño < 0:
                conexion.sendall("¡Ganaste!\n".encode())
                print(f"El cliente {num_cliente} ha ganado")
                break
            else:
                conexion.sendall(f"Jugador {num_cliente}, Da un paso. Contador restante: {tamaño}\n".encode())
    
    conexion.close()

def aceptar_conexiones():
    global clientes

    for num_cliente in range(1, 3):
        conexion, direccion = serverSocket.accept()
        print(f"Jugador {num_cliente} conectado desde {direccion}")

        clientes.append(conexion)

        hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion, num_cliente))
        hilo.start()


aceptar_conexiones()
serverSocket.close()

