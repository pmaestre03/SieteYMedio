from random import *
import pymysql
from variables import *

conn = pymysql.connect(host="51.145.227.94", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

settings_game = {'n_players':0}

#Recibe una lista y un bool y crea un menu en base a la lista
def crearMenu(lista,separador,empezarEnCero = True,lJust = 0):
    for i in range(len(lista)):
        if empezarEnCero:
            cadena = str(i) + separador+ str(lista[i])
        else:
            cadena = str(i+1) + separador + str(lista[i])
        print("".ljust(lJust)+cadena)

#Recibe un texto a centrar, el numero al cual quiere centrar y, opcionalmente, un caracter para rellenar los laterales
def crearTitulo(titulo,centroNumero,centroCaracter = False):
    if centroCaracter:
        print(titulo.center(centroNumero, centroCaracter))
    else:
        print(titulo.center(centroNumero))

#Sirve para limpiar la terminal
def limpiarTerminal():
    print("\n" * 100)

#Nos permite controlar todos los parametros permitidos en un input (excepto textos con caracteres entre medio)
def comprobarInput(textoInput,lJust=0,soloText = True, soloNum = False,tuplaRangoNumeros = (), letras_num = False, permitirCaractEspeciales = False,excepciones=[]):
    while True:
        opcion = input("".ljust(lJust)+textoInput)
        if opcion in excepciones:
            return opcion
        if opcion.isspace() or opcion == "":
            input("Introduce algo\nPulsa enter para continuar")
        elif soloText:
            if opcion.isalpha():
                return opcion
            else:
                input("Solo puedes introducir letras\nPulsa enter para continuar")
        elif soloNum:
            if opcion.isnumeric():
                if len(tuplaRangoNumeros) != 0:
                    minimo = tuplaRangoNumeros[0]; maximo = tuplaRangoNumeros[1];
                    if int(opcion) >= minimo and int(opcion) <= maximo:
                        return opcion
                    else:
                        input("Solo puedes introducir numeros entre "+str(minimo)+" y "+str(maximo)+"\nPulsa enter para continuar")
                else:
                    return opcion
            else:
                input("Solo puedes introducir numeros\nPulsa enter para continuar")
        elif letras_num:
            if opcion.isalnum():
                return opcion
            else:
                input("Solo puedes introducir letras y numeros\nPulsa enter para continuar")
        elif permitirCaractEspeciales:
            if not opcion.isalnum() or opcion.isalnum():
                return opcion
            else:
                input("Error\nPulsa enter para continuar")

def printSevenAndHalfTitle(mensajeFinal):
    print("="*140+"\n"+
"                 #####                                          #                         #     #                        \n"
"                 #     #  ######  #    #  ######  #    #        # #    #    #  #####       #     #    ##    #       ######\n"
"                 #        #       #    #  #       ##   #       #   #   ##   #  #    #      #     #   #  #   #       #     \n"
"                  #####   #####   #    #  #####   # #  #      #     #  # #  #  #    #      #######  #    #  #       ##### \n"
"                       #  #       #    #  #       #  # #      #######  #  # #  #    #      #     #  ######  #       #     \n"
"                 #     #  #        #  #   #       #   ##      #     #  #   ##  #    #      #     #  #    #  #       #     \n"
"                  #####   ######    ##    ######  #    #      #     #  #    #  #####       #     #  #    #  ######  #     \n"+
mensajeFinal.center(140,"=")+"\n"
)
def mostrarPlayers():
    cursorHumanos = conn.cursor()
    cursorBots = conn.cursor()

    cadena = 'Select Players'.center(140,'*')+'\n'+'Boot Player'.center(69,' ')+'||'+'Player Player'.center(69,' ')+'\n'+'-'*140+'\n'+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(24)+"||".ljust(1)+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(25)+"\n"+"*"*140
    print(cadena)

    queryHumanos = f"select * from player where human = 1"
    queryBot = f"select * from player where human = 0"

    cursorHumanos.execute(queryHumanos)
    cursorBots.execute(queryBot)

    while True:
        h = cursorHumanos.fetchone()
        b = cursorBots.fetchone()

        if type(h) == type(None) and type(b) == type(None):
            break
        if type(h) == type(None):
            bList = list(b)
            cadena = bList[0].ljust(19)+" "+bList[1].ljust(24)+" "+reisgoEnTexto(bList[2]).ljust(24) + "||".ljust(1)
        elif type(b) == type(None):
            hList = list(h)
            cadena = "||".ljust(1) + hList[0].ljust(19)+" "+hList[1].ljust(24)+" "+reisgoEnTexto(hList[2]).ljust(25)
        else:
            hList = list(h)
            bList = list(b)
            cadena = bList[0].ljust(19)+" "+bList[1].ljust(24)+" "+reisgoEnTexto(bList[2]).ljust(24) + "||".ljust(1) + hList[0].ljust(19)+" "+hList[1].ljust(24)+" "+reisgoEnTexto(hList[2]).ljust(25)
        print(cadena)
    print("*"*140)

def reisgoEnTexto(riesgo):
                if riesgo == 30:
                    return "Prudente"
                elif riesgo == 40:
                    return "Normal"
                elif riesgo == 50:
                    return "Atrevido"
                else:
                    return str(riesgo)

def newRandomDNI():
    while True:
        dniNumero = randint(11111111,99999999)
        dniLetra = "TRWAGMYFPDXBNJZSQVHLCKE"[dniNumero % 23]
        dni = f"{dniNumero}{dniLetra}"

        if checkExistenceDNI(dni):
            return dni

def checkExistenceDNI(dni):
    query = f"select * from player where dni = '{dni}'"
    cur.execute(query)
    if cur.fetchall():
        return False
    else:
        return True

def checkExistenceName(name):
    query = f"select * from player where name = '{name}'"
    cur.execute(query)
    
    if not cur.fetchall():
        return True
    else:
        return False

def returnBarajaMezclada(mazo):
    baraja = []
    for i in mazo:
        baraja.append(i)
    
    shuffle(baraja)
    return baraja


#Players conf functions
def playersConf():
    while True:
        limpiarTerminal()
        printSevenAndHalfTitle("")
        crearTitulo("Añadir/Eliminar/Mostrar Jugadores",107)
        crearMenu(["Nuevo jugador","Nuevo Bot","Mostrar/Quitar jugadores","Atras"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,4))

        if opcion == "1":
            newPlayer()
        elif opcion == "2":
            newPlayer(esBot=True)
        elif opcion == "3":
            showPlayersAndRemove()
        else:
            break

def newPlayer(esBot=False):

    limpiarTerminal()
    printSevenAndHalfTitle("")

    titulo = "Nuevo Jugador Humano"
    if esBot:
        titulo = "Nuevo Jugador Bot"

    crearTitulo(titulo,107)

    if esBot:
        dni = newRandomDNI()
    else:
        dni = comp_dni("Introduce tu dni: ")
    
    while True:

        name = comprobarInput("Introduce el nombre: ",soloText=False,letras_num=True)

        if not checkExistenceName(name):
            print("Este nombre ya existe")
        else:
            break

    riesgo = selectLevelRisc()

    if comprobacion_fin(dni,name,riesgo):
        checkHuman = 1
        if esBot:
            checkHuman = 0
        query = f"INSERT INTO player VALUES ('{dni}','{name}',{riesgo},{checkHuman})"
        cur.execute(query)
        conn.commit()
        input("Jugador creado correctamente\nPulsa enter para continuar")



def comp_dni(textoInput):
    lista = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    try:
        nif = input(textoInput)
        if len(nif) == 9:
            if nif[:8].isdigit() and nif[8:].isalpha():
                if nif[8:].lower() == lista[int(nif[:8]) % 23].lower():
                    if not checkExistenceDNI(nif):
                        raise ValueError('Este DNI ya existe')
                    else:
                        return str(nif)
                else:
                    raise ValueError('La letra del DNI no es correcta')
            else:
                raise ValueError('El DNI debe tener 8 numeros y una letra')
        else:
            raise ValueError('EL DNI debe tener 9 caracteres')
    except ValueError as e:
        print(e)
        return comp_dni("Introduce tu dni: ")

def selectLevelRisc():
    cadena = 'Escoge un nivel de riesgo\n1) Atrevido \n2) Normal\n3) Prudente\n'
    print(cadena)
    opc = comprobarInput(textoInput='> ',soloText=False,soloNum=True,tuplaRangoNumeros=(1,3))
    if opc == "1":
        return 50
    if opc == "2":
        return 40
    if opc == "3":
        return 30

def comprobacion_fin(dni,name,level_risc):
    if level_risc == 30:
        level_risc = "Prudente"
    elif level_risc == 40:
        level_risc = "Normal"
    else:
        level_risc = "Atrevido"
    cadena = 'DNI'.ljust(10)+''+str(dni).rjust(30)+'\n'+ 'Nombre'.ljust(10)+''+str(name).rjust(30)+'\n'+ 'Nivel de Riesgo'.ljust(10)+''+level_risc.rjust(25)+'\n'
    print(cadena)
    opc = input('Es correcto? S/n\n> ')
    if opc.lower() == 's':
        return True
    else:
        return False

def showPlayersAndRemove():
    while True:
        limpiarTerminal()
        mostrarPlayers()
        print("-ID para eliminar jugador | 0 para volver atras".center(140))
        entrada = input(" "*46+"> ")
        
        if entrada[0] == "-" and not checkExistenceDNI(entrada[1:]):
            query = f"delete from player where dni = '{entrada[1:]}'"
            cur.execute(query)
            conn.commit()
        elif entrada == "0":
            break
        else:
            input("Pon un ID valido y en formato correcto\nPulsa enter para continuar")

    
#Settings functions
def settings():
    global settings_game

    try:
        cartas = settings_game["deck"]
    except:
        cartas = cartasES

    try:
        rondas = settings_game["n_rouds"]
    except:
        rondas = 5

    limpiarTerminal()
    
    while True:
        printSevenAndHalfTitle(" Configuración ")
        crearMenu(["Seleccionar Jugadores","Seleccionar Baraja de Cartas","Seleccionar Maximo Rondas (5 Rondas por Defecto)","Atras"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,4))

        if opcion == "1":
            players = setGamePlayers()
            settings_game["n_players"] = len(players)
            settings_game["players"] = players
        elif opcion == "2":
            cartas = setCardsDeck()
            settings_game["deck"] = cartas
        elif opcion == "3":
            rondas = setMaxRounds()
            settings_game["n_rouds"] = rondas
        else:
            settings_game["deck"] = cartas
            settings_game["n_rouds"] = rondas
            return

def mostrarPlayers_settings(players_in_game_list=[]):
    cursorHumanos = conn.cursor()
    cursorBots = conn.cursor()

    cadena = 'Select Players'.center(140, '*') + '\n' + 'Boot Player'.center(69, ' ') + '||' + 'Player Player'.center(
        69, ' ') + '\n' + '-' * 140 + '\n' + "ID".ljust(20) + "Name".ljust(25) + "Type".ljust(24) + "||".ljust(
        1) + "ID".ljust(20) + "Name".ljust(25) + "Type".ljust(25) + "\n" + "*" * 140
    print(cadena)

    queryHumanos = f"select * from player where human = 1"
    queryBot = f"select * from player where human = 0"
    l_h,l_b = [],[]
    human = cursorHumanos.execute(queryHumanos)
    bot = cursorBots.execute(queryBot)
    for i in range(int(human)):
        h = cursorHumanos.fetchone()
        l_h.append(h)
    for i in range(int(bot)):
        b = cursorBots.fetchone()
        l_b.append(b)
    while True:
        cadena1 = ''
        if len(l_b)>0:
            while True:
                print(l_b[0][0])
                if l_b[0][0] not in players_in_game_list:
                    cadena1 += l_b[0][0].ljust(19) + " " + l_b[0][1].ljust(24) + " " + reisgoEnTexto(l_b[0][2]).ljust(24) + "||".ljust(1)
                    break
                else:
                    break           
        if len(l_h)>0:
            while True:
                if l_h[0][0] not in players_in_game_list:
                    cadena1 += l_h[0][0].ljust(19) + " " + l_h[0][1].ljust(24) + " " + reisgoEnTexto(l_h[0][2]).ljust(25)
                    break
                else:
                    break
        l_b, l_h = l_b[1:], l_h[1:]
        print(l_b,l_h)

        print(cadena1)
        if len(l_h)== 0 and len(l_b) == 0:
            break
    print('a')
    print("*" * 140)

def lis_dic(players_in_game):
    query = f"select * from player"
    cur.execute(query)
    players = cur.fetchall()
    dict_players = {} 
    for i in players_in_game:
        for j in players:
            if i == j[0]:
                if j[3] == 1:
                    dict_players[i]={"name":j[1],"human":True,"priority":0,"type":j[2],"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"","roundPoints":0}
                if j[3] == 0:
                    dict_players[i]={"name":j[1],"human":False,"priority":0,"type":j[2],"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"","roundPoints":0}
    return dict_players
    
def player_in_game(players_in_game=[]):
    query = f"select * from player"
    cur.execute(query)
    players = cur.fetchall()
    pjs= []
    for i in players:
        pjs.append(i)
    cadena = ' Jugadores Actuales en la Partida '.center(70,'*').center(140,' ')
    print(cadena)
    
    if len(players_in_game) == 0:
        print('No hay Jugadores'.center(140,' '))
    else:
        query = f"select * from player"
        cur.execute(query)
        players = cur.fetchall()

        pjs= []
        for i in players:
            pjs.append(i)

        for i in players_in_game:
            for j in pjs:
                if j[0] == i:
                    if j[3] == 1:
                        cadena = (j[0].ljust(16)+" "+j[1].ljust(22)+" "+'Humano'.ljust(16)+reisgoEnTexto(j[2]).ljust(23)).center(150,' ')
                    if j[3] == 0:
                        cadena = (j[0].ljust(16)+" "+j[1].ljust(22)+" "+'Boot'.ljust(16)+reisgoEnTexto(j[2]).ljust(23)).center(150,' ')
                    print(cadena)  
    input()

def lis_dic(players_in_game):
    query = f"select * from player"
    cur.execute(query)
    players = cur.fetchall()

    dict_players = {}

    for i in players_in_game:
        for j in players:
            if i == j[0]:
                if j[3] == 1:
                    dict_players[i]={"name":j[1],"human":True,"bank":False,"initialCard":"","priority":0 ,"type":j[2],"bet":0,"points":20,"cards":[],"roundPoints":0}
                if j[3] == 0:
                    dict_players[i]={"name":j[1],"human":False,"bank":False,"initialCard":"","priority":0 ,"type":j[2],"bet":0,"points":20,"cards":[],"roundPoints":0}
    return dict_players

def setGamePlayers():
        selecion = True
        limpiarTerminal()

        players_in_game=[]
        player_in_game(players_in_game)
        
        limpiarTerminal()
        printSevenAndHalfTitle(' Selecciona un Jugador o Bot para Agregar a la Partida ')

        while selecion:
            mostrarPlayers_settings(players_in_game_list=players_in_game)

            while True:
                print("".ljust(6)+"Opciones: id para añadir a la partida, -id para eliminar de la partida, sh para mostrar los jugadores en partida, -1 para salir")
                option = comprobarInput("> ",lJust=6,soloText=False,permitirCaractEspeciales=True,excepciones=['-1'])
                if option[0]== '-' and option[1:] in players_in_game:
                    input('the player {} is erased of the game\npress any botton to continue'.format(option[1:]))
                    players_in_game.remove(option[1:])
                    break

                elif not checkExistenceDNI(option):
                    if not option in players_in_game:
                        players_in_game.append(option)
                    else:
                        input("Ese ID no es valido\nPulsa enter para continuar")
                    break

                elif option == '-1':
                    player_in_game(players_in_game=players_in_game)
                    selecion = False
                    break
                elif option == "sh":
                    player_in_game(players_in_game)
                elif len(players_in_game) == 6:
                    player_in_game(players_in_game=players_in_game)
                    selecion = False
                    break   
                else:
                    input("Ese ID no es valido\nPulsa enter para continuar")
            if not selecion:
                break
            player_in_game(players_in_game=players_in_game)
            limpiarTerminal()
        return lis_dic(players_in_game)


def setCardsDeck():
    while True:
        printSevenAndHalfTitle(' Selecciona la Baraja ')
        crearMenu(["Baraja Española","Baraja de Poker","Atras"],") ",empezarEnCero=False)
        opcion = int(comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,3)))
        if opcion == 1:
            return cartasES
        if opcion == 2:
            return cartasPoker
        else:
            try:
                return settings_game["deck"]
            except:
                return cartasES
    
def setMaxRounds():
    printSevenAndHalfTitle('')
    while True:
        rounds = int(comprobarInput("Selecciona el Maximo de Rondas a Jugar\n> ",soloText = False,soloNum=True,tuplaRangoNumeros=(5,30)))
        option = comprobarInput("Seguro que quieres que sean {} rondas? S/n\n> ".format(rounds),letras_num=True)
        if option.lower() == 's':
            return rounds
#Play Functions
def burbujaPrioridad(lista):
    cartas = settings_game['deck']

    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):

            numero1 = cartas[lista[j]]["realValue"]
            numero2 = cartas[lista[j+1]]["realValue"]

            if numero1 < numero2:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            elif numero1 == numero2:

                numero1 = cartas[lista[j]]["priority"]
                numero2 = cartas[lista[j+1]]["priority"]

                if numero1 < numero2:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

def generarPrioridad():
    players = settings_game["players"]

    player_in_game = list(players.keys())

    mazo = returnBarajaMezclada(settings_game["deck"])

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

#settings_game = {'n_players':len(players),'players':players,'n_rounds':rondas,'deck':cartas}

def ordenar_prioridad():
    lista = []
    for i in settings_game["players"]:
        lista.append(settings_game["players"][i]['priority'])

    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero
    return lista

def mesa(lista):
    players = settings_game["players"]

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

def uno_en_mesa(lista,players):
    for i in players:
        si = list(players[i].keys())
    cadena = ''
    for h in si:
        cadena += str(h).ljust(20).title()
        for j in lista:
            cadena += str(players[j][h]).ljust(50)
        cadena+='\n'
    print(cadena)

def pedirSegunRasgo(cartasEnBaraja,mazo,rasgo, roundPoints):
    cartasPasarse = 0
    for carta in cartasEnBaraja:
        valorCarta = mazo[carta]["realValue"]
        if roundPoints + valorCarta > 7.5:
            cartasPasarse += 1
    
    cartasPorSalir = len(cartasEnBaraja)
    formula = (cartasPasarse/cartasPorSalir)*100
    if formula > rasgo:
        return False
    else:
        return True

def turnoBot(cartasEnBaraja,mazo,puntos,rasgo):
    if puntos == 0 or puntos == 0.5:
        return True
    else:
        return pedirSegunRasgo(cartasEnBaraja,mazo,rasgo,puntos)

def autoPlayBot(baraja,mazo,rasgo,jugador):
    while True:
        roundPoints = settings_game["players"][jugador]["roundPoints"]

        if turnoBot(baraja,mazo,roundPoints,rasgo):
            elemento0 = baraja[0]

            settings_game["players"][jugador]["roundPoints"] += cartasES[elemento0]["value"]

            settings_game["players"][jugador]["cards"].append(elemento0)

            baraja.remove(elemento0)
        else:
            break

def listarPuntosJugadores(dicPlayers):
    listaPuntosJugadores = []
    for i in dicPlayers:
        listaPuntosJugadores.append(dicPlayers[i]["roundPoints"])
    return listaPuntosJugadores
def listarApuestasJugadores(dicPlayers):
    listaApuestaJugadores = []
    for i in dicPlayers:
        listaApuestaJugadores.append(dicPlayers[i]["bet"])
    return listaApuestaJugadores
def sumarApuestasJugadores(dicPlayers):
    sumaApuestaJugadores = 0
    for i in dicPlayers:
        sumaApuestaJugadores += dicPlayers[i]["bet"]
    return sumaApuestaJugadores

def decisionBancaPedir(cartasEnBaraja,mazo,roundPoints,rasgo,puntos,players):
    listaPuntosJugadores = listarPuntosJugadores(players)
    listaApuestaJugadores = listarApuestasJugadores(players)
    sumaPuntosApostados = sumarApuestasJugadores(players)

    if roundPoints == 7.5:
        return False
    elif roundPoints < 7.5:
        
        totalPuntosRepartir = 0

        for i in range(len(listaPuntosJugadores)-1):
            if roundPoints < listaPuntosJugadores[i]:
                totalPuntosRepartir += listaApuestaJugadores[i]

        #Porque eso significa que ha ganado a todos los players
        if totalPuntosRepartir == 0:
            return False

        #Esto significa que no supera a ningun jugador
        elif sumaPuntosApostados == totalPuntosRepartir:
            return True

        #Esto significa si despues de repartir los puntos se queda sin
        elif totalPuntosRepartir >= puntos:
            return True

        #Esto significa si despues de repartir los puntos aun tiene
        elif totalPuntosRepartir < puntos:
            return pedirSegunRasgo(cartasEnBaraja,mazo,rasgo,roundPoints)

    elif roundPoints == 0 or roundPoints == 0.5:
        return True
    else:
        return pedirSegunRasgo(cartasEnBaraja,mazo,rasgo,roundPoints)


def autoPlayBanca(baraja,mazo,rasgo,jugador,roundPoints,puntos,players):
    print(len(baraja))
    input()
    print(mazo)
    input()
    print(rasgo)
    input()
    print(jugador)
    input()
    print(roundPoints)
    input()
    print(puntos)
    input()
    print(players)
    input()
    while True:
        roundPoints = settings_game["players"][jugador]["roundPoints"]

        if decisionBancaPedir(baraja,mazo,roundPoints,rasgo,puntos,players):
            elemento0 = baraja[0]

            settings_game["players"][jugador]["roundPoints"] += cartasES[elemento0]["value"]

            settings_game["players"][jugador]["cards"].append(elemento0)

            baraja.remove(elemento0)
        else:
            break

def menuJuegoHumano():
    crearMenu(["Estadisticas","Estadisticas Partida","Hacer Apuesta","Pedir Carta","Jugar Automatico","Plantarse"],") ",empezarEnCero=False,lJust=59)

    opcion = comprobarInput("Opcion: ",lJust=59,soloText=False,soloNum=True,tuplaRangoNumeros=(1,6))

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

def play():
    if settings_game["n_players"] < 2:
        input("Debes al menos 2 jugadores en la partida para poder empezar\nPulsa enter para continuar")
    else:
        
        generarPrioridad()
        listaPrioridad = ordenar_prioridad()

        mazo = settings_game["deck"]
        players = settings_game["players"]
        
        for ronda in range(settings_game["n_rouds"]):
            baraja = returnBarajaMezclada(settings_game["deck"])

            for prioridadJugador in listaPrioridad:

                for jugador in settings_game["players"]:
                    if settings_game["players"][jugador]["priority"] == prioridadJugador:

                        limpiarTerminal()
                        printSevenAndHalfTitle(f"Ronda {ronda}, Turno de {settings_game['players'][jugador]['name']}")

                        rasgo = settings_game["players"][jugador]["type"]
                        roundPoints = settings_game["players"][jugador]["roundPoints"]
                        puntos = settings_game["players"][jugador]["points"]

                        if settings_game["players"][jugador]["human"] == False:
                            if settings_game["players"][jugador]["bank"] == True:
                                autoPlayBanca(baraja,mazo,rasgo,jugador,roundPoints,puntos,players)
                            else:

                                autoPlayBot(baraja,mazo,rasgo,jugador)
                            
                        else:
                            if settings_game["players"][jugador]["bank"] == True:
                                menuJuegoHumano()
                                print(jugador)
                            else:
                                menuJuegoHumano()
                                print(jugador)
                        uno_en_mesa([jugador],players)
                        input()
        #no te olvides de resetear el diccionario

#Ranking functions
def ranking():
    limpiarTerminal()
    while True:
        printSevenAndHalfTitle(" Clasificación ")
        crearMenu(["Jugadores con más Puntos","Jugadores con más Partidas Jugadas","Jugadores con más Minutos Jugados","Atras"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,4))

        if opcion == "1":
            showPlayersWithMoreEarning()
        elif opcion == "2":
            showPlayersWithMoreGamesPlayed()
        elif opcion == "3":
            showPlayersWithMoreMinutesPlayed()
        else:
            break

def showPlayersWithMoreEarning():
    print("PWME")

def showPlayersWithMoreGamesPlayed():
    print("PWMGP")

def showPlayersWithMoreMinutesPlayed():
    print("PWMMP")

#Reports Functions
def reports():
    limpiarTerminal()
    while True:
        printSevenAndHalfTitle(" Reportes ")
        crearMenu(["Esto","Aun","Esta","Por","Acabar","Porfavor","Sal","Go back"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,8))

        if opcion == "1":
            print("nada")
        elif opcion == "8":
            break
