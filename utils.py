from random import *
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
def comprobarInput(textoInput, soloNum = False,tuplaRangoNumeros = (), letras_num = False, permitirCaractEspeciales = False):
    while True:
        opcion = input(textoInput)
        if opcion.isspace() or opcion == "":
            input("Introduce algo\nPulsa enter para continuar")
        elif not soloNum:
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

def playersConf():
    print("Players conf")

def settings():
    print("Settings")

def play():
    print("Play")

def ranking():
    print("Ranking")

def reports():
    print("Reports")

def newRandomDNI():
    dniNumero = randint(11111111,99999999)
    dniLetra = "TRWAGMYFPDXBNJZSQVHLCKE"[dniNumero % 23]

    #Habria que comprobar si el DNI aleatorio existe en la BBDD
    return f"{dniNumero}{dniLetra}"