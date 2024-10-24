# Juego del 21 o BlackJack
# Ignacio Delgado Alias Ignacio Drako
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
        print("Te has excedido. Pierdes.")
        return True
    elif suma_contrario > 21:
        print("El contrario se ha excedido. Ganas.")
        return True
    else:
        return False

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

# Función principal del juego
def juego():
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
            print("1.-Pedir carta")
            print("2.-Plantarse")
            try:
                opcion = int(input("Elije una opcion: "))
            except ValueError:
                print("Opción no válida. Inténtalo de nuevo.")
                continue
            if opcion == 1:
                carta = repartir_carta(mazo)
                cartasPj.append(carta)
                print("========================================")
                print("Carta: ", carta)
                print("========================================")
                print("Cartas del jugador: ", cartasPj)
                print("========================================")
                print("Cartas del contrario: ", cartasia)
                print("========================================")
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                if control(suma_jugador, suma_contrario):
                    break
                if len(cartasPj) == 2:
                    TurnoPj = False
            elif opcion == 2:
                TurnoPj = False
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        else:
            if len(cartasia) == 0:
                carta = repartir_carta(mazo)
                cartasia.append(carta)
                carta = repartir_carta(mazo)
                cartasia.append(carta)
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                if control(suma_jugador, suma_contrario):
                    break
                TurnoPj = True
            elif len(cartasia) == 1:
                carta = repartir_carta(mazo)
                cartasia.append(carta)
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                if control(suma_jugador, suma_contrario):
                    break
                TurnoPj = True
            elif len(cartasia) == 2:
                suma_jugador = calcular_suma(cartasPj)
                print("========================================")
                print("Suma jugador: ", suma_jugador)
                print("========================================")
                suma_contrario = calcular_suma(cartasia)
                print("========================================")
                print("Suma contrario: ", suma_contrario)
                print("========================================")
                if control(suma_jugador, suma_contrario):
                    break
                if suma_jugador > suma_contrario:
                    print("========================================")
                    print("Gana el jugador")
                    print("========================================")
                    break
                elif suma_jugador < suma_contrario:
                    print("Gana el contrario")
                    break
                else:
                    print("Empate")
                    break

# Bucle principal para jugar continuamente
while True:
    print("Bienvenido al juego del 21 o BlackJack")
    print("1.-Jugar")
    print("2.-Salir")
    try:
        opcion = int(input("Elije una opcion: "))
    except ValueError:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    if opcion == 1:
        juego()
    elif opcion == 2:
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
