# Juego del 21 o BlackJack
# Ignacio Delgado Alias Ignacio Drako

cartasPj = []  # cartas que tiene el jugador
cartasia = []  # cartas que tiene el contrario
corazones = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # las cartas de cada palo
diamantes = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
treboles = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
picas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
jp_juega = True  # variable para controlar al jugador
ia_juega = False  # variable para controlar el juego
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
mazo = [corazones, diamantes, treboles, picas]  # mazo de cartas
TurnoPj = True  # turno del jugador, si falso turno del rival
# Función para calcular la suma de las cartas
def calcular_suma(cartas):
    total = 0
    ases = 0
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
# Menú
print("Bienvenido al juego del 21 o BlackJack")
print("1.-Jugar")
print("2.-Salir")
opcion = int(input("Elije una opcion: "))
if opcion == 1:
    while True:
        if TurnoPj:
            print("Cartas del jugador: ", cartasPj)
            print("Cartas del contrario: ", cartasia)
            print("1.-Pedir carta")
            print("2.-Plantarse")
            opcion = int(input("Elije una opcion: "))
            if opcion == 1:
                carta = mazo[0][0]
                cartasPj.append(carta)
                mazo[0].remove(carta)
                print("Carta: ", carta)
                print("Cartas del jugador: ", cartasPj)
                print("Cartas del contrario: ", cartasia)
                if len(cartasPj) == 2:
                    TurnoPj = False
            elif opcion == 2:
                TurnoPj = False
        else:
            if len(cartasia) == 0:
                carta = mazo[0][0]
                cartasia.append(carta)
                mazo[0].remove(carta)
                carta = mazo[0][0]
                cartasia.append(carta)
                mazo[0].remove(carta)
                suma_jugador = calcular_suma(cartasPj)
                suma_contrario = calcular_suma(cartasia)
                print("Cartas del jugador: ", suma_jugador)
                print("Suma del jugador: ", cartasia)
                print("Cartas del contrario: ", cartasia)
                print("Suma contrario: ", suma_contrario)
                TurnoPj = True
            elif len(cartasia) == 1:
                carta = mazo[0][0]
                cartasia.append(carta)
                mazo[0].remove(carta)
                print("Cartas del jugador: ", cartasPj)
                print("Cartas del contrario: ", cartasia)
                TurnoPj = True
            elif len(cartasia) == 2:
                suma_jugador = calcular_suma(cartasPj)
                print("Suma jugador: ", suma_jugador)
                suma_contrario = calcular_suma(cartasia)
                print("Suma contrario: ", suma_contrario)
                if suma_jugador > suma_contrario:
                    print("Gana el jugador")
                    break
                elif suma_jugador < suma_contrario:
                    print("Gana el contrario")
                    break
                else:
                    print("Empate")
                    break
def ia_robar_carta():#si es menor a 17 roba carta, si es 21 se planta, si es mayor a 21 pierde
    if suma_contrario == 21:
        return False
    elif suma_contrario <= 20:
        return True
    else:
        return ia_pierde True
def control():#si el jugador se pasa de 21 pierde
    if suma_jugador > 21:
        print("Te has excedido")
        return True
    else:
        return False
