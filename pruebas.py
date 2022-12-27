import pymysql

conn = pymysql.connect(host="51.145.227.94", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()
query = f"select * from player"
cur.execute(query)
var = list(cur.fetchall())

for pasadas in range(len(var) - 1):
    for comp in range(len(var) - 1 - pasadas):
        if var[comp][1] < var[comp + 1][1]:
            var[comp], var[comp + 1] = var[comp + 1], var[comp]
for i in var:
    listaOrd = f'{i}'
    print(listaOrd)
input()

cadena = 'select Players'.center(140,'*')+'\n'+'Boot Player'.center(69,' ')+'||'+'Player Player'.center(69,' ')+'\n'+'-'*140+'\n'+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(24)+"||".ljust(1)+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(25)+"\n"+"*"*140
print(cadena)
bot = []
player = []
for i in players:
        if i[3]== 1:
            player.append(i)
        else:
            bot.append(i)
print(bot)
print(player)
max = 0
if len(bot) > len(player):
    max = len(bot)
if len(bot) < len(player):
    max = len(player)
if len(bot) == len(player):
    max = len(bot)

cadena = ''
for i in range(int(max)+1):
    if i < len(bot) and i < len(player):
        cadena += str(bot[i-1][0]).ljust(20)+str(bot[i-1][1]).ljust(25)+str(bot[i-1][2]).ljust(24)+"||".ljust(1)+str(player[i-1][0]).ljust(20)+str(player[i-1][1]).ljust(25)+str(player[i-1][0]).ljust(25)+'\n'     
    if i <= len(player) and i > len(bot):
            cadena += ' '*69+"||".ljust(1)+str(player[i-1][0]).ljust(20)+str(player[i-1][1]).ljust(25)+str(player[i-1][0]).ljust(25)+'\n'
    if i <= len(bot) and i > len(player):
            cadena += str(bot[i-1][0]).ljust(20)+str(bot[i-1][1]).ljust(25)+str(bot[i-1][2]).ljust(24)+"||".ljust(1)+' '*69+'\n'   