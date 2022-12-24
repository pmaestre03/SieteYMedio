from random import *
import pymysql

conn = pymysql.connect(host="51.145.227.94", user="pnaharro", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()



#Recibe una lista y un bool y crea un menu en base a la lista
def crearMenu(lista,separador,empezarEnCero = True):
    for i in range(len(lista)):
        if empezarEnCero:
            print(str(i) + separador+ str(lista[i]))
        else:
            print(str(i+1) + separador + str(lista[i]))

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
def comprobarInput(textoInput,soloText = True, soloNum = False,tuplaRangoNumeros = (), letras_num = False, permitirCaractEspeciales = False):
    while True:
        opcion = input(textoInput)
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
            if not opcion.isalnum():
                return opcion
            else:
                input("Puedes poner lo que te salga de los huevos y aun asi fallas, que sujeto tan estupido\nPulsa enter para continuar")

def printSevenAndHalfTitle(mensajeFinal):
    print("="*107+"\n"+
"  #####                                          #                         #     #                        \n"
" #     #  ######  #    #  ######  #    #        # #    #    #  #####       #     #    ##    #       ######\n"
" #        #       #    #  #       ##   #       #   #   ##   #  #    #      #     #   #  #   #       #     \n"
"  #####   #####   #    #  #####   # #  #      #     #  # #  #  #    #      #######  #    #  #       ##### \n"
"       #  #       #    #  #       #  # #      #######  #  # #  #    #      #     #  ######  #       #     \n"
" #     #  #        #  #   #       #   ##      #     #  #   ##  #    #      #     #  #    #  #       #     \n"
"  #####   ######    ##    ######  #    #      #     #  #    #  #####       #     #  #    #  ######  #     \n"+
mensajeFinal.center(107,"=")+"\n"
)

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
    
    if not cur.fetchall():
        return True
    else:
        return False

def checkExistenceName(name):
    query = f"select * from player where name = '{name}'"
    cur.execute(query)
    
    if not cur.fetchall():
        return True
    else:
        return False
    

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
        dni = comp_dni()
    
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



def comp_dni():
    lista = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    try:
        nif = input('Introduce tu dni: ')
        if len(nif) == 9:
            if nif[:8].isdigit() and nif[8:].isalpha():
                if nif[8:].lower() == lista[int(nif[:8]) % 23].lower():
                    if not checkExistenceDNI(nif):
                        raise ValueError('Este DNI ya existe')
                    else:
                        print(nif)
                        return str(nif)
                else:
                    raise ValueError('La letra del DNI no es correcta')
            else:
                raise ValueError('El DNI debe tener 8 numeros y una letra')
        else:
            raise ValueError('EL DNI debe tener 9 caracteres')
    except ValueError as e:
        print(e)
        return comp_dni()

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

    limpiarTerminal()
    printSevenAndHalfTitle("")

    query = f"select * from player"
    cur.execute(query)
    variable = cur.fetchall()

    input("Seguro? ")
    for i in variable:
        print(i)
    input()
    
#Settings functions
def settings():
    limpiarTerminal()
    while True:
        printSevenAndHalfTitle(" Settings ")
        crearMenu(["Set Game Players","Set Card's Deck","Set Max Rounds (Default 5 Rounds)","Go back"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,4))

        if opcion == "1":
            setGamePlayers()
        elif opcion == "2":
            setCardsDeck()
        elif opcion == "3":
            setMaxRounds()
        else:
            break

def setGamePlayers():
    print("SGP")

def setCardsDeck():
    print("SCD")

def setMaxRounds():
    print("SMR")

#Play Functions
def play():
    print("Play")

#Ranking functions
def ranking():
    limpiarTerminal()
    while True:
        printSevenAndHalfTitle(" Ranking ")
        crearMenu(["Players With More Earnings","Players With More Games Played","Players With More Minutes Played","Go back"],") ",empezarEnCero=False)

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
        printSevenAndHalfTitle(" Ranking ")
        crearMenu(["Esto","Aun","Esta","Por","Acabar","Porfavor","Sal","Go back"],") ",empezarEnCero=False)

        opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,8))

        if opcion == "1":
            print("nada")
        elif opcion == "8":
            break


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