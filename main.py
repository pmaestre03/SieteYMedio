from utils import *
from random import *

#Ejemplo de uso de pymysql
'''
import pymysql
conn=pymysql.connect(host="51.145.227.94",user="prius",password="P@ssw0rd",db="proyecto")
cur = conn.cursor()
query = f"select * from aventura"
cur.execute(query)
variable = cur.fetchall
'''
2
while True:
    limpiarTerminal()
    printSevenAndHalfTitle("")
    crearMenu(["Add/Remove/Show Players","Settings","Play Game","Ranking","Reports","Exit"],") ",empezarEnCero=False)

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
        print("Good Bye!!!")
        break