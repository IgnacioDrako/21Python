import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))  # Cambia "127.0.0.1" por la IP del servidor en la red local

while True:
    response = client.recv(4096).decode()
    print(response, flush=True)  # Asegurarse de que el mensaje se imprima inmediatamente
    if "Gana" in response or "Pierdes" in response or "Empate" in response:
        break
    opcion = input()
    client.sendall(opcion.encode())