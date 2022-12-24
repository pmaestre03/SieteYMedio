import pymysql

conn = pymysql.connect(host="51.145.227.94", user="pnaharro", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()
cor = conn.cursor()


cadena = 'select Players'.center(140,'*')+'\n'+'Boot Player'.center(69,' ')+'||'+'Player Player'.center(69,' ')+'\n'+'-'*140+'\n'+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(24)+"||".ljust(1)+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(25)+"\n"+"*"*140
print(cadena)


queryHumanos = f"select * from player where human = 1"
queryBot = f"select * from player where human = 0"

cur.execute(queryHumanos)
cor.execute(queryBot)

while True:
    h = cur.fetchone()
    b = cor.fetchone()

    #"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(24)+"||".ljust(1)+"ID".ljust(20)+"Name".ljust(25)+"Type".ljust(25)

    if type(h) == type(None) and type(b) == type(None):
        break
    if type(h) == type(None):
        bList = list(b)
        cadena = bList[0].ljust(19)+" "+bList[1].ljust(24)+" "+str(bList[2]).ljust(24) + "||".ljust(1)
    elif type(b) == type(None):
        hList = list(h)
        cadena = "||".ljust(1) + hList[0].ljust(19)+" "+hList[1].ljust(24)+" "+str(hList[2]).ljust(25)
    else:
        hList = list(h)
        bList = list(b)
        cadena = bList[0].ljust(19)+" "+bList[1].ljust(24)+" "+str(bList[2]).ljust(24) + "||".ljust(1) + hList[0].ljust(19)+" "+hList[1].ljust(24)+" "+str(hList[2]).ljust(25)
    print(cadena)
print("*"*140)
