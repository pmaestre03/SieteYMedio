from random import *
from utils import *

cartasES = {
    "O01": {"literal": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
    "O02": {"literal": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
    "O03": {"literal": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
    "O04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
    "O05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
    "O06": {"literal": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
    "O07": {"literal": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
    "O08": {"literal": "Sota de Oros", "value": 0.5, "priority": 4, "realValue": 8},
    "O09": {"literal": "Caballo de Oros", "value": 0.5, "priority": 4, "realValue": 9},
    "O10": {"literal": "Rey de Oros", "value": 0.5, "priority": 4, "realValue": 10},
    "C01": {"literal": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
    "C02": {"literal": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
    "C03": {"literal": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
    "C04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
    "C05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
    "C06": {"literal": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
    "C07": {"literal": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
    "C08": {"literal": "Sota de Copas", "value": 0.5, "priority": 3, "realValue": 8},
    "C09": {"literal": "Caballo de Copas", "value": 0.5, "priority": 3, "realValue": 9},
    "C10": {"literal": "Rey de Copas", "value": 0.5, "priority": 3, "realValue": 10},
    "E01": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    "E02": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    "E03": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    "E04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    "E05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
    "E06": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    "E07": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    "E08": {"literal": "Sota de Espadas", "value": 0.5, "priority": 2, "realValue": 8},
    "E09": {"literal": "Caballo de Espadas", "value": 0.5, "priority": 2, "realValue": 9},
    "E10": {"literal": "Rey de Espadas", "value": 0.5, "priority": 2, "realValue": 10},
    "B01": {"literal": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
    "B02": {"literal": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
    "B03": {"literal": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
    "B04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
    "B05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
    "B06": {"literal": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
    "B07": {"literal": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
    "B08": {"literal": "Sota de Bastos", "value": 0.5, "priority": 1, "realValue": 8},
    "B09": {"literal": "Caballo de Bastos", "value": 0.5, "priority": 1, "realValue": 9},
    "B10": {"literal": "Rey de Bastos", "value": 0.5, "priority": 1, "realValue": 10},
}

cartas = cartasES
players = {
"11115555A":{"name":"Mario","human":True,"priority":0,"type":40,"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"",
"roundPoints":0},
"22225555A":{"name":"Pedro","human":True,"priority":0,"type":40,"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"",
"roundPoints":0},
"22225554A":{"name":"jose","human":True,"priority":0,"type":40,"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"",
"roundPoints":0},
"22225553A":{"name":"marcos","human":True,"priority":0,"type":40,"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"",
"roundPoints":0}
}

def burbujaPrioridad(lista):

    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):

            numero1 = cartas[lista[j]]["value"]
            numero2 = cartas[lista[j+1]]["value"]

            if numero1 < numero2:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            elif numero1 == numero2:

                numero1 = cartas[lista[j]]["priority"]
                numero2 = cartas[lista[j+1]]["priority"]

                if numero1 < numero2:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

def generarPrioridad():
    player_in_game = list(players.keys())

    mazo = []
    for i in cartas:
        mazo.append(i)

    shuffle(mazo)

    cartasIniciales = []
    for i in range(len(player_in_game)):
        jugadorActual = player_in_game[i]
        players[jugadorActual]["initialCard"] = mazo[i]

        cartasIniciales.append(mazo[i])

    burbujaPrioridad(cartasIniciales)

    for i in range(len(player_in_game)):
        jugadorActual = player_in_game[i]
        cartaInicalJugador = players[jugadorActual]["initialCard"]
        players[jugadorActual]["priority"] = len(cartasIniciales) - cartasIniciales.index(cartaInicalJugador)
        if players[jugadorActual]["priority"] == len(cartasIniciales):
            players[jugadorActual]["bank"] = True


def ordenar_prioridad():
    lista = []
    for i in players:
        lista.append(players[i]['priority'])

    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero
    return lista


def mesa(lista):
    for i in players:
        si = list(players[i].keys())
    cadena = ''
    for h in si:
        cadena += str(h).ljust(20).title()
        for j in range(3):
            for i in players:
                if lista[j] == players[i]['priority']:
                    cadena += str(players[i][h]).ljust(50)
        cadena+='\n'
    print(cadena)
    print('-'*140)
    cadena = ''
    lista=lista[3:]
    for h in si:
        cadena += str(h).ljust(20).title()
        for j in lista:
            for i in players:
                if j == players[i]['priority']:
                    cadena += str(players[i][h]).ljust(50)
        cadena+='\n'
    print(cadena)



def decisionBot(cartasEnBaraja,mazo, puntos, rasgo, banca=False):
    if puntos == 0 or puntos == 0.5:
        return True
    else:
        cartasNoPasarse = 0
        cartasPasarse = 0
        for carta in cartasEnBaraja:
            valorCarta = mazo[carta]["realValue"]
            if puntos + valorCarta > 7.5:
                cartasPasarse += 1
            else:
                cartasNoPasarse += 1
        
        CartasPorSalir = len(cartasEnBaraja)
        formula = (cartasPasarse/CartasPorSalir)*100
        if formula > rasgo:
            return False
        else:
            return True

def returnBarajaMezclada(mazo):
    baraja = []
    for i in mazo:
        baraja.append(i)
    
    shuffle(baraja)
    return baraja



def menuJuegoHumano():
    crearMenu(["Estadisticas","Estadisticas Partida","Hacer Apuesta","Pedir Carta","Jugar Automatico","Plantarse"],") ",empezarEnCero=False,lJust=30)

    opcion = comprobarInput("Opcion: ",lJust=30,soloText=False,soloNum=True,tuplaRangoNumeros=(1,6))

    if opcion == "1":
        print("stats")
    elif opcion == "2":
        print("game stats")
    elif opcion == "3":
        print("bet")
    elif opcion == "4":
        print("order")
    elif opcion == "5":
        print("autoplay")
    elif opcion == "6":
        print("stand")
    
def uno_en_mesa(lista):
    for i in players:
        si = list(players[i].keys())
    cadena = ''
    for h in si:
        cadena += str(h).ljust(20).title()
        for j in lista:
            cadena += str(players[j][h]).ljust(50)
        cadena+='\n'
    print(cadena)
generarPrioridad()
lista = ['11115555A']
uno_en_mesa(lista)