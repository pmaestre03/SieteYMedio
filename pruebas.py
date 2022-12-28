import pymysql
conn=pymysql.connect(host="51.145.227.94",user="prius",password="P@ssw0rd",db="proyecto")
cur = conn.cursor()

query = f"select * from player"
cur.execute(query)
players = cur.fetchall()


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
