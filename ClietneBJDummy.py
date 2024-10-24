import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.3.80", 9999))

while True:
    response = client.recv(4096).decode()
    print(response)
    if "Gana" in response or "Pierdes" in response or "Empate" in response:
        break
    opcion = input()
    client.sendall(opcion.encode())