import socket
import threading
def listen_to_server(client_socket):
    while True:
        try:
            response = client_socket.recv(4096).decode()
            if not response:
                break
            print(response, flush=True)  # Asegurarse de que el mensaje se imprima inmediatamente
            if "Gana" in response or "Pierdes" in response or "Empate" in response:
                break
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            break
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))  # Cambia "127.0.0.1" por la IP del servidor en la red local

    # Crear un hilo para escuchar continuamente los mensajes del servidor
    listener_thread = threading.Thread(target=listen_to_server, args=(client,))
    listener_thread.start()

    while True:
        try:
            opcion = input()
            client.sendall(opcion.encode())
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            break
if __name__ == "__main__":
    main()