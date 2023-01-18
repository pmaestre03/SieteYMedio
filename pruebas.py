import pymysql
from utils import *
from random import *
#conn=pymysql.connect(host="51.145.227.94",user="prius",password="P@ssw0rd",db="proyecto")
#cur = conn.cursor()

#query = f"select * from player"
#cur.execute(query)
#players = cur.fetchall()
player = {
"11115555A":{"name":"Mario","human":True,"priority":1,"type":40,"bank":True,"bet":5,"points":20,"cards":[],"initialCard":"","roundPoints":5},
"22225555A":{"name":"Pedro","human":True,"priority":2,"type":30,"bank":False,"bet":2,"points":20,"cards":[],"initialCard":"","roundPoints":7.5},
"22225554A":{"name":"jose","human":True,"priority":3,"type":50,"bank":False,"bet":2,"points":20,"cards":[],"initialCard":"","roundPoints":7.5},
"22225553A":{"name":"marcos","human":True,"priority":4,"type":40,"bank":False,"bet":6,"points":20,"cards":[],"initialCard":"","roundPoints":6}
}

#dict_players[i]={"name":j[1],"human":True,"priority":0,"type":j[2],"bank":False,"bet":0,"points":0,"cards":[],"initialCard":"","roundPoints":0}

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
        if players[i]['roundPoints'] > bank[1] and players[i]['roundPoints'] <= 7.5:
            if players[i]['roundPoints'] == 7.5:
                puntos_a_dar[i] = players[i]['roundPoints'] * 2 
            else:
                puntos_a_dar[i] = players[i]['roundPoints']
    if len(puntos_a_dar) > 0:
        for i in puntos_a_dar:
            if players[bank[0]]['points'] > 0:
                if(players[bank[0]]['points'] - puntos_a_dar[i]) <= 0:
                    players[i]['points'] += players[bank[0]]['points']
                    players[bank[0]]['points'] = 0
                else:
                    players[bank[0]]['points'] -= puntos_a_dar[i]
                    players[i]['points'] += puntos_a_dar[i]
    for i in players:
        if players[i]['roundPoints'] <= players[bank[0]]['roundPoints'] or players[i]['roundPoints'] > 7.5:
            if player[i] != player[bank[0]]: 
                if (players[i]['points'] - players[i]['bet']) <=0:
                    players[i]['points'] = 0
                    players[bank[0]]['points']+= players[i]['points']
                else:
                    players[i]['points'] -= players[i]['bet']
                    players[bank[0]]['points']+= players[i]['bet']
    siete_medio = []
    for i in player:
        if player[i]['roundPoints'] == 7.5:
            siete_medio.append(i)
    if len(siete_medio) >= 1:
        if len(siete_medio) == 1:
            player[siete_medio[0]]['bank'] == True
            player[bank[0]]['bank'] = False
        else:
            lista = []
            for i in siete_medio:
                lista.append(player[i]['priority'])
            for i in range(len(lista) - 1):
                for j in range(len(lista) - i - 1):
                    if lista[j] < lista[j + 1]:
                        numero = lista[j]
                        lista[j] = lista[j + 1]
                        lista[j + 1] = numero
            for i in player:
                if player[i]['priority'] == lista[0]:
                    player[i]['bank'] = True
                    player[bank[0]]['bank'] = False
    for i in player:
        player[i]['roundPoints'] = 0
        player[i]['cards'] = []
        player[i]['bet'] = 0
    deletes= []
    for i in player:
        if player[i]['points'] == 0:
            deletes.append(i)
    for i in deletes:
        player.pop(i)
   
    return players

player = repartir_puntos(player)
for i in player:
        print(i,player[i]) 