from random import *
import pymysql
from variables import *

conn = pymysql.connect(host="51.145.227.94", user="pmaestre", password="P@ssw0rd", db="proyecto")
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
                if l_b[0][0] not in players_in_game_list:
                    cadena1 += l_b[0][0].ljust(19) + " " + l_b[0][1].ljust(24) + " " + reisgoEnTexto(l_b[0][2]).ljust(24) + "||".ljust(1)
                    break
                else:
                    #cadena1 += "".ljust(69) + "||".ljust(1)
                    try:
                        if len(l_b) > 1:
                            l_b = l_b[1:]
                        else:
                            raise
                    except:
                        cadena1 += "".ljust(69) + "||".ljust(1)
                        break
        if len(l_h)>0:
            while True:
                if l_h[0][0] not in players_in_game_list:
                    cadena1 += l_h[0][0].ljust(19) + " " + l_h[0][1].ljust(24) + " " + reisgoEnTexto(l_h[0][2]).ljust(25)
                    break
                else:
                    try:
                        if len(l_h) > 1:
                            l_h = l_h[1:]
                        else:
                            raise
                    except:
                        break
                    
        l_b,l_h = l_b[1:],l_h[1:]

        print(cadena1)
        if len(l_h)== 0 and len(l_b) == 0:
            break
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
                if len(players_in_game) == 6:
                    player_in_game(players_in_game=players_in_game)
                    selecion = False
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

def ordenar_prioridad_inGame():
    lista = []
    for i in settings_game["players"]:
        if settings_game["players"][i]["bank"] == False:
            lista.append(settings_game["players"][i]['priority'])

    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero
            
    for i in settings_game["players"]:
        if settings_game["players"][i]["bank"] == True:
            lista.append(settings_game["players"][i]['priority'])
    return lista

def mesa(lista):
    players = settings_game["players"]

    for i in players:
        si = list(players[i].keys())
    cadena = ''
    if len(lista) >= 3:
        for h in si:
            cadena += str(h).ljust(20).title()
            for j in range(3):
                for i in players:
                    if lista[j] == players[i]['priority']:
                        cadena += str(players[i][h]).ljust(50)
            cadena+='\n'
        print(cadena)
        if len(lista) >= 4:
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
    else:
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

def apostarPuntosBot(players,player,rasgo,puntos):
    if players[player]["bet"] == 0:
        if players[player]["points"] == 1:
            players[player]["bet"] = 1
        else:
            apuesta = puntos * (rasgo/100)
            players[player]["bet"] = int(apuesta)
    return players

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
        if not dicPlayers[i]["bank"]:
            listaPuntosJugadores.append(dicPlayers[i]["roundPoints"])
    return listaPuntosJugadores
def listarApuestasJugadores(dicPlayers):
    listaApuestaJugadores = []
    for i in dicPlayers:
        if not dicPlayers[i]["bank"]:
            listaApuestaJugadores.append(dicPlayers[i]["bet"])
    return listaApuestaJugadores
def sumarApuestasJugadores(dicPlayers):
    sumaApuestaJugadores = 0
    for i in dicPlayers:
        if not dicPlayers[i]["bank"]:
            sumaApuestaJugadores += dicPlayers[i]["bet"]
    return sumaApuestaJugadores

def decisionBancaPedir(cartasEnBaraja,mazo,roundPoints,rasgo,puntos,players):
    listaPuntosJugadores = listarPuntosJugadores(players)
    listaApuestaJugadores = listarApuestasJugadores(players)
    sumaPuntosApostados = sumarApuestasJugadores(players)

    if roundPoints == 7.5:
        return False
    if roundPoints == 0 or roundPoints == 0.5:
        return True
    elif roundPoints < 7.5:
        
        totalPuntosRepartir = 0

        for i in range(len(listaPuntosJugadores)):
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
    else:
        return pedirSegunRasgo(cartasEnBaraja,mazo,rasgo,roundPoints)

def repartir_puntos(players):
    bank = []
    puntos_a_dar = {}
    for i in players:
        if players[i]['bank'] == True:
            bank.append(i)
            bank.append(players[i]['roundPoints'])
    for i in players:
        if bank[1] == 7.5:
            break
        if players[i]['roundPoints'] > bank[1] and players[i]['roundPoints'] <= 7.5 or players[bank[0]]["roundPoints"] > 7.5:
            if players[i]['roundPoints'] == 7.5:
                puntos_a_dar[i] = players[i]['bet'] * 2
            else:
                puntos_a_dar[i] = players[i]['bet']
    if len(puntos_a_dar) > 0:
        for i in puntos_a_dar:
            if players[bank[0]]['roundPoints'] > 0 and players[bank[0]]['roundPoints'] <= 7.5:
                if(players[bank[0]]['points'] - puntos_a_dar[i]) <= 0:
                    players[i]['points'] += players[bank[0]]['points']
                    players[bank[0]]['points'] = 0
                else:
                    players[bank[0]]['points'] -= puntos_a_dar[i]
                    players[i]['points'] += puntos_a_dar[i]
            if players[bank[0]]["roundPoints"] > 7.5:
                if(players[bank[0]]['points'] - puntos_a_dar[i]) <= 0:
                    players[i]['points'] += players[bank[0]]['points']
                    players[bank[0]]['points'] = 0
                else:
                    players[bank[0]]['points'] -= puntos_a_dar[i]
                    players[i]['points'] += puntos_a_dar[i]
    for i in players:
        if players[bank[0]]['roundPoints'] > 7.5:
            break
        if players[i]['roundPoints'] <= players[bank[0]]['roundPoints'] or players[i]['roundPoints'] > 7.5:
            if players[i] != players[bank[0]]: 
                if (players[i]['points'] - players[i]['bet']) <=0:
                    players[i]['points'] = 0
                    players[bank[0]]['points']+= players[i]['points']
                else:
                    players[i]['points'] -= players[i]['bet']
                    players[bank[0]]['points']+= players[i]['bet']
    siete_medio = []
    if players[bank[0]]['points'] <= 0:
        lista = []
        for i in players:
            if i != bank[0]:
                lista.append(players[i]['priority'])
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
        for i in players:
            if players[i]['priority'] == lista[0]:
                players[i]['bank'] = True
                players[bank[0]]['bank'] = False
    else:
        for i in players:
            if players[i]['roundPoints'] == 7.5 and players[i]["bank"] == False:
                siete_medio.append(i)
        if len(siete_medio) >= 1:
            if len(siete_medio) == 1:
                players[siete_medio[0]]['bank'] = True
                players[bank[0]]['bank'] = False
            else:
                lista = []
                for i in siete_medio:
                    lista.append(players[i]['priority'])
                for i in range(len(lista) - 1):
                    for j in range(len(lista) - i - 1):
                        if lista[j] < lista[j + 1]:
                            numero = lista[j]
                            lista[j] = lista[j + 1]
                            lista[j + 1] = numero
                for i in players:
                    if players[i]['priority'] == lista[0]:
                        players[i]['bank'] = True
                        players[bank[0]]['bank'] = False
    for i in players:
        players[i]['roundPoints'] = 0
        players[i]['cards'] = []
        players[i]['bet'] = 0
    deletes= []
    for i in players:
        if players[i]['points'] == 0:
            deletes.append(i)
    for i in deletes:
        players.pop(i)
    return players

def autoPlayBanca(baraja,mazo,rasgo,jugador,roundPoints,puntos,players):
    while True:
        roundPoints = players[jugador]["roundPoints"]

        if decisionBancaPedir(baraja,mazo,roundPoints,rasgo,puntos,players):
            elemento0 = baraja[0]

            players[jugador]["roundPoints"] += mazo[elemento0]["value"]

            players[jugador]["cards"].append(elemento0)

            baraja.remove(elemento0)
        else:
            break
    return players

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

                for jugador in players:
                    if players[jugador]["priority"] == prioridadJugador:

                        limpiarTerminal()
                        printSevenAndHalfTitle(f"Ronda {ronda}, Turno de {settings_game['players'][jugador]['name']}")

                        rasgo = players[jugador]["type"]
                        roundPoints = players[jugador]["roundPoints"]
                        puntos = players[jugador]["points"]

                        if players[jugador]["human"] == False:
                            if players[jugador]["bank"] == True:
                                players = autoPlayBanca(baraja,mazo,rasgo,jugador,roundPoints,puntos,players)

                            else:
                                players = apostarPuntosBot(players,jugador,rasgo,puntos)
                                autoPlayBot(baraja,mazo,rasgo,jugador)
                            
                        else:
                            if players[jugador]["bank"] == True:
                                menuJuegoHumano()

                            else:
                                menuJuegoHumano()
                        mesa(listaPrioridad)
                        #uno_en_mesa([jugador],players)
                        input()
        #no te olvides de resetear el diccionario
            players = repartir_puntos(players)
            listaPrioridad = ordenar_prioridad_inGame()
            print(listaPrioridad)
            input()

#Ranking functions
def ranking():
    limpiarTerminal()
    while True:
        printSevenAndHalfTitle(" Clasificación ")
        crearMenu(["Jugadores con más Puntos","Jugadores con más Partidas Jugadas","Jugadores con más Minutos Jugados","Atras"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText = False,soloNum=True,tuplaRangoNumeros=(1,4))

        if opcion == "1":
            showPlayersWithMoreEarning()
        elif opcion == "2":
            showPlayersWithMoreGamesPlayed()
        elif opcion == "3":
            showPlayersWithMoreMinutesPlayed()
        else:
            break

def showPlayersWithMoreEarning():
    query = f"select * from scores"
    cur.execute(query)
    scores = cur.fetchall()
    var = list(scores)
    for pasadas in range(len(var)-1):
            for comp in range(len(var)-1-pasadas):
                if var[comp][2] < var[comp+1][2]:
                    var[comp],var[comp+1] = var[comp+1],var[comp]
    for i in var:
        listaOrd = f'{i}'
        print(listaOrd)
    input()
    print("PWME")

def showPlayersWithMoreGamesPlayed():
    query = f"select * from scores"
    cur.execute(query)
    scores = cur.fetchall()
    var = list(scores)
    for pasadas in range(len(var)-1):
        for comp in range(len(var)-1-pasadas):
            if var[comp][3] < var[comp+1][3]:
                var[comp],var[comp+1] = var[comp+1],var[comp]
    for i in var:
        listaOrd = f'{i}'
        print(listaOrd)
    print("PWMGP")

def showPlayersWithMoreMinutesPlayed():
    query = f"select * from scores"
    cur.execute(query)
    scores = cur.fetchall()
    var = list(scores)
    for pasadas in range(len(var)-1):
            for comp in range(len(var)-1-pasadas):
                if var[comp][4] < var[comp+1][4]:
                    var[comp],var[comp+1] = var[comp+1],var[comp]
    for i in var:
        listaOrd = f'{i}'
        print(listaOrd)
    input()
    print("PWMMP")

#Reports Functions
def reports():
    limpiarTerminal()
    while True:
        printSevenAndHalfTitle(" Reportes ")
        crearMenu(["Initial card more repeated by each user, only users who have played a minimum of 3 games.","Player who makes the highest bet per game, find the round with the highest bet."
        ,"Player who makes the lowest bet per game.","Percentage of rounds won per player in each game (%), as well as their average bet for the game.",
        "List of games won by Bots.","Rounds won by the bank in each game.","Number of users have been the bank in each game.","Average bet per game.",
        "Average bet of the first round of each game.","Average bet of the last round of each game.","Go back"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,11))
        if opcion == "1" or opcion == "4" or opcion == "6":
            print("Not implemented")
            input()
        if opcion == "2":
            rep_prop2()
        if opcion == "3":
            rep_prop3()
        if opcion == "5":
            rep_prop5()
        if opcion == "7":
            rep_prop7()
        if opcion == "8":
            rep_prop8()
        if opcion == "9":
            rep_prop9()
        if opcion == "10":
            rep_prop10()
        elif opcion == "11":
            break

def rep_prop2():
    prop2 = conn.cursor()
    queryprop2 = f"select g.id_game,gp.dni,r.points_bet from games g inner join game_player gp on g.id_game = gp.id_game inner join round r on gp.dni = r.dni where r.points_bet = (select max(r.points_bet) from round)"
    prop2.execute(queryprop2)
    propuesta2 = list(prop2.fetchall())
    print(propuesta2)
    input()
    return

def rep_prop3():
    prop3 = conn.cursor()
    queryprop3 = f"select g.id_game,gp.dni,r.points_bet from games g inner join game_player gp on g.id_game = gp.id_game inner join round r on gp.dni = r.dni where r.points_bet = (select min(r.points_bet)from round);"
    prop3.execute(queryprop3)
    propuesta3 = list(prop3.fetchall())
    print(propuesta3)
    input()
    return

def rep_prop5():
    prop5 = conn.cursor()
    queryprop5 = f"select w.id_game,w.points from winners w inner join player p on w.dni = p.dni where p.human = 0;"
    prop5.execute(queryprop5)
    propuesta5 = list(prop5.fetchall())
    print(propuesta5)
    input()
    return

def rep_prop7():
    prop7 = conn.cursor()
    queryprop7 = f"select g.id_game,count(distinct dni) as banca from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round where r.bank = 1 group by g.id_game;"
    prop7.execute(queryprop7)
    propuesta7 = list(prop7.fetchall())
    print(propuesta7)
    input()
    return

def rep_prop8():
    prop8 = conn.cursor()
    queryprop8 = f"select g.id_game,avg(r.points_bet) as media_puntos_partida from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round group by rg.id_game;"
    prop8.execute(queryprop8)
    propuesta8 = list(prop8.fetchall())
    print(propuesta8)
    input()
    return

def rep_prop9():
    prop9 = conn.cursor()
    queryprop9 = f"select g.id_game,avg(r.points_bet) as media from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round where rg.id_round = 1 group by rg.id_round_games;"
    prop9.execute(queryprop9)
    propuesta9 = list(prop9.fetchall())
    print(propuesta9)
    input()
    return

def rep_prop10():
    prop10 = conn.cursor()
    queryprop10 = f"select g.id_game,avg(r.points_bet) as media_ultima_ronda from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round where rg.id_round = (select max(rg.id_round) from round_games) group by rg.id_round_games;"
    prop10.execute(queryprop10)
    propuesta10 = list(prop10.fetchall())
    print(propuesta10)
    input()
    return
###############################################################################################################
#Variables

cartas = {
    "O01": {"literal": "As de Oros", "value": 1, "priority": 4, "realValue": 1},
    "O02": {"literal": "Dos de Oros", "value": 2, "priority": 4, "realValue": 2},
    "O03": {"literal": "Tres de Oros", "value": 3, "priority": 4, "realValue": 3},
    "O04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
    "O05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
    "O06": {"literal": "Seis de Oros", "value": 6, "priority": 4, "realValue": 6},
    "O07": {"literal": "Siete de Oros", "value": 7, "priority": 4, "realValue": 7},
    "O08": {"literal": "Sota de Oros", "value": 8, "priority": 4, "realValue": 0.5},
    "O09": {"literal": "Caballo de Oros", "value": 9, "priority": 4, "realValue": 0.5},
    "O10": {"literal": "Rey de Oros", "value": 10, "priority": 4, "realValue": 0.5},
    "C01": {"literal": "As de Copas", "value": 1, "priority": 3, "realValue": 1},
    "C02": {"literal": "Dos de Copas", "value": 2, "priority": 3, "realValue": 2},
    "C03": {"literal": "Tres de Copas", "value": 3, "priority": 3, "realValue": 3},
    "C04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
    "C05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
    "C06": {"literal": "Seis de Copas", "value": 6, "priority": 3, "realValue": 6},
    "C07": {"literal": "Siete de Copas", "value": 7, "priority": 3, "realValue": 7},
    "C08": {"literal": "Sota de Copas", "value": 8, "priority": 3, "realValue": 0.5},
    "C09": {"literal": "Caballo de Copas", "value": 9, "priority": 3, "realValue": 0.5},
    "C10": {"literal": "Rey de Copas", "value": 10, "priority": 3, "realValue": 0.5},
    "E01": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    "E02": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    "E03": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    "E04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    "E05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
    "E06": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    "E07": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    "E08": {"literal": "Sota de Espadas", "value": 8, "priority": 2, "realValue": 0.5},
    "E09": {"literal": "Caballo de Espadas", "value": 9, "priority": 2, "realValue": 0.5},
    "E10": {"literal": "Rey de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
    "B01": {"literal": "As de Bastos", "value": 1, "priority": 1, "realValue": 1},
    "B02": {"literal": "Dos de Bastos", "value": 2, "priority": 1, "realValue": 2},
    "B03": {"literal": "Tres de Bastos", "value": 3, "priority": 1, "realValue": 3},
    "B04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
    "B05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
    "B06": {"literal": "Seis de Bastos", "value": 6, "priority": 1, "realValue": 6},
    "B07": {"literal": "Siete de Bastos", "value": 7, "priority": 1, "realValue": 7},
    "B08": {"literal": "Sota de Bastos", "value": 8, "priority": 1, "realValue": 0.5},
    "B09": {"literal": "Caballo de Bastos", "value": 9, "priority": 1, "realValue": 0.5},
    "B10": {"literal": "Rey de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
}

cartasP = {
    "AC": {"literal": "As de Corazones", "value": 1, "priority": 4, "realValue": 1},
    "2C": {"literal": "Dos de Corazones", "value": 2, "priority": 4, "realValue": 2},
    "3C": {"literal": "Tres de Corazones", "value": 3, "priority": 4, "realValue": 3},
    "4C": {"literal": "Cuatro de Corazones", "value": 4, "priority": 4, "realValue": 4},
    "5C": {"literal": "Cinco de Corazones", "value": 5, "priority": 4, "realValue": 5},
    "6C": {"literal": "Seis de Corazones", "value": 6, "priority": 4, "realValue": 6},
    "7C": {"literal": "Siete de Corazones", "value": 7, "priority": 4, "realValue": 7},
    "8C": {"literal": "Ocho de Corazones", "value": 8, "priority": 4, "realValue": 0.5},
    "9C": {"literal": "Nueve de Corazones", "value": 9, "priority": 4, "realValue": 0.5},
    "10C": {"literal": "Diez de Corazones", "value": 10, "priority": 4, "realValue": 0.5},
    "JC": {"literal": "Jota de Corazones", "value": 11, "priority": 4, "realValue": 0.5},
    "QC": {"literal": "Reina de Corazones", "value": 12, "priority": 4, "realValue": 0.5},
    "KC": {"literal": "Rey de Corazones", "value": 13, "priority": 4, "realValue": 0.5},
    "AD": {"literal": "As de Diamantes", "value": 1, "priority": 3, "realValue": 1},
    "2D": {"literal": "Dos de Diamantes", "value": 2, "priority": 3, "realValue": 2},
    "3D": {"literal": "Tres de Diamantes", "value": 3, "priority": 3, "realValue": 3},
    "4D": {"literal": "Cuatro de Diamantes", "value": 4, "priority": 3, "realValue": 4},
    "5D": {"literal": "Cinco de Diamantes", "value": 5, "priority": 3, "realValue": 5},
    "6D": {"literal": "Seis de Diamantes", "value": 6, "priority": 3, "realValue": 6},
    "7D": {"literal": "Siete de Diamantes", "value": 7, "priority": 3, "realValue": 7},
    "8D": {"literal": "Ocho de Diamantes", "value": 8, "priority": 3, "realValue": 0.5},
    "9D": {"literal": "Nueve de Diamantes", "value": 9, "priority": 3, "realValue": 0.5},
    "10D": {"literal": "Diez de Diamantes", "value": 10, "priority": 3, "realValue": 0.5},
    "JD": {"literal": "Jota de Diamantes", "value": 11, "priority": 3, "realValue": 0.5},
    "QD": {"literal": "Reina de Diamantes", "value": 12, "priority": 3, "realValue": 0.5},
    "KD": {"literal": "Rey de Diamantes", "value": 13, "priority": 3, "realValue": 0.5},
    "AS": {"literal": "As de Espadas", "value": 1, "priority": 2, "realValue": 1},
    "2S": {"literal": "Dos de Espadas", "value": 2, "priority": 2, "realValue": 2},
    "3S": {"literal": "Tres de Espadas", "value": 3, "priority": 2, "realValue": 3},
    "4S": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
    "5S": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
    "6S": {"literal": "Seis de Espadas", "value": 6, "priority": 2, "realValue": 6},
    "7S": {"literal": "Siete de Espadas", "value": 7, "priority": 2, "realValue": 7},
    "8S": {"literal": "Ocho de Espadas", "value": 8, "priority": 2, "realValue": 0.5},
    "9S": {"literal": "Nueve de Espadas", "value": 9, "priority": 2, "realValue": 0.5},
    "10S": {"literal": "Diez de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
    "JS": {"literal": "Jota de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
    "QS": {"literal": "Reina de Espadas", "value": 12, "priority": 2, "realValue": 0.5},
    "KS": {"literal": "Rey de Espadas", "value": 13, "priority": 2, "realValue": 0.5},
    "AH": {"literal": "As de Tréboles", "value": 1, "priority": 1, "realValue": 1},
    "2H": {"literal": "Dos de Tréboles", "value": 2, "priority": 1, "realValue": 2},
    "3H": {"literal": "Tres de Tréboles", "value": 3, "priority": 1, "realValue": 3},
    "4H": {"literal": "Cuatro de Tréboles", "value": 4, "priority": 1, "realValue": 4},
    "5H": {"literal": "Cinco de Tréboles", "value": 5, "priority": 1, "realValue": 5},
    "6H": {"literal": "Seis de Tréboles", "value": 6, "priority": 1, "realValue": 6},
    "7H": {"literal": "Siete de Tréboles", "value": 7, "priority": 1, "realValue": 7},
    "8H": {"literal": "Ocho de Tréboles", "value": 8, "priority": 1, "realValue": 0.5},
    "9H": {"literal": "Nueve de Tréboles", "value": 9, "priority": 1, "realValue": 0.5},
    "10H": {"literal": "Diez de Tréboles", "value": 10, "priority": 1, "realValue": 0.5},
    "JH": {"literal": "Jota de Tréboles", "value": 11, "priority": 1, "realValue": 0.5},
    "QH": {"literal": "Reina de Tréboles", "value": 12, "priority": 1, "realValue": 0.5},
    "KH": {"literal": "Rey de Tréboles", "value": 13, "priority": 1, "realValue": 0.5},
}
