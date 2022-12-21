from utils import *


while True:
    opcion = False

    crearTitulo("Texto", 20, "=")

    crearMenu(["Sumar","Restar","Multiplicar","Dividir","Salir"],empezarEnCero=False)

    opcion = comprobarInput("Opcion: ",soloNum=True,tuplaRangoNumeros=(1,5))


    if opcion == "1":
        suma()
    elif opcion == "2":
        resta()
    elif opcion == "3":
        multiplicacion()
    elif opcion == "4":
        division()
    else:
        print("Saliendo...")
        break