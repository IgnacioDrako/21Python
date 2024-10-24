import socket
import threading
import random

# Función para repartir una carta aleatoria del mazo
def repartir_carta(mazo):
    palo = random.choice(mazo)
    carta = random.choice(palo)
    palo.remove(carta)
    return carta

# Corrección de la función ia_robar_carta
def ia_robar_carta(suma_contrario):
    if suma_contrario >= 21:
        return False
    elif suma_contrario < 21:
        return True
    else:
        return False

# Corrección de la función control
def control(suma_jugador, suma_contrario):
    if suma_jugador > 21:
        return "Te has excedido. Pierdes."
    elif suma_contrario > 21:
        return "El contrario se ha excedido. Ganas."
    else:
        return None

# Función para calcular la suma de las cartas
def calcular_suma(cartas):
    total = 0
    ases = 0
    values = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }
    for carta in cartas:
        if carta == "A":
            ases += 1
        else:
            total += values[carta]
    
    # Añadir los ases al total, considerando que pueden valer 1 o 11
    for _ in range(ases):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total

# Función para manejar la conexión con un cliente
def handle_client(client_socket):
    global cartasPj, cartasia, mazo, TurnoPj
    cartasPj = []  # cartas que tiene el jugador
    cartasia = []  # cartas que tiene el contrario
    corazones = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # las cartas de cada palo
    diamantes = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    treboles = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    picas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    mazo = [corazones, diamantes, treboles, picas]  # mazo de cartas
    TurnoPj = True  # turno del jugador, si falso turno del rival

    while True:
        if TurnoPj:
            client_socket.sendall(b"1.-Pedir carta\n2.-Plantarse\nElije una opcion: ")
            opcion = client_socket.recv(1024).decode().strip()
            if opcion == "1":
                carta = repartir_carta(mazo)
                cartasPj.append(carta)
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                resultado = control(suma_jugador, suma_contrario)
                client_socket.sendall(f"Tu mano: {cartasPj}, Valor: {suma_jugador}\n".encode())
                client_socket.sendall(f"Mano del rival: {cartasia}, Valor: {suma_contrario}\n".encode())
                if resultado:
                    client_socket.sendall(resultado.encode())
                    break
                if len(cartasPj) == 2:
                    TurnoPj = False
            elif opcion == "2":
                TurnoPj = False
            else:
                client_socket.sendall("Opción no válida. Inténtalo de nuevo.\n".encode('utf-8'))
        else:
            if len(cartasia) == 0:
                carta = repartir_carta(mazo)
                cartasia.append(carta)
                carta = repartir_carta(mazo)
                cartasia.append(carta)
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                resultado = control(suma_jugador, suma_contrario)
                client_socket.sendall(f"Tu mano: {cartasPj}, Valor: {suma_jugador}\n".encode())
                client_socket.sendall(f"Mano del rival: {cartasia}, Valor: {suma_contrario}\n".encode())
                if resultado:
                    client_socket.sendall(resultado.encode())
                    break
                TurnoPj = True
            elif len(cartasia) == 1:
                carta = repartir_carta(mazo)
                cartasia.append(carta)
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                resultado = control(suma_jugador, suma_contrario)
                client_socket.sendall(f"Tu mano: {cartasPj}, Valor: {suma_jugador}\n".encode())
                client_socket.sendall(f"Mano del rival: {cartasia}, Valor: {suma_contrario}\n".encode())
                if resultado:
                    client_socket.sendall(resultado.encode())
                    break
                TurnoPj = True
            elif len(cartasia) == 2:
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                resultado = control(suma_jugador, suma_contrario)
                client_socket.sendall(f"Tu mano: {cartasPj}, Valor: {suma_jugador}\n".encode())
                client_socket.sendall(f"Mano del rival: {cartasia}, Valor: {suma_contrario}\n".encode())
                if resultado:
                    client_socket.sendall(resultado.encode())
                    break
                if suma_jugador > suma_contrario:
                    client_socket.sendall(b"Gana el jugador\n")
                    break
                elif suma_jugador < suma_contrario:
                    client_socket.sendall(b"Gana el contrario\n")
                    break
                else:
                    client_socket.sendall(b"Empate\n")
                    break

# Configuración del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(5)
print("Servidor escuchando en el puerto 9999")

while True:
    client_socket, addr = server.accept()
    print(f"Conexión aceptada de {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()