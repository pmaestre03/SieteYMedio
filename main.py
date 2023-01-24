from utils import *
from random import *

while True:
    limpiarTerminal()
    printSevenAndHalfTitle("")
    crearMenu(["Añadir/Eliminar/Mostrar Jugadores","Configuración","Jugar","Clasificación","Reportes","Salir"],") ",empezarEnCero=False)

    opcion = comprobarInput("> ",soloText=False,soloNum=True,tuplaRangoNumeros=(1,6))

    if opcion == "1":
        playersConf()
    elif opcion == "2":
        settings()
    elif opcion == "3":
        play()
    elif opcion == "4":
        ranking()
    elif opcion == "5":
        reports()
    else:
        print("Adiós!!!")
        break
