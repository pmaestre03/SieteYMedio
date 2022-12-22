from utils import *
from random import *

while True:

    printSevenAndHalfTitle("")
    crearMenu(["Add/Remove/Show Players","Settings","Play Game","Ranking","Reports","Exit"],") ",empezarEnCero=False)

    option = comprobarInput("> ",soloNum=True,tuplaRangoNumeros=(1,6))


    if option == "1":
        playersConf()
        print(newRandomDNI())
    elif option == "2":
        settings()
    elif option == "3":
        play()
    elif option == "4":
        ranking()
    elif option == "5":
        reports()
    else:
        print("Good Bye!!!")
        break