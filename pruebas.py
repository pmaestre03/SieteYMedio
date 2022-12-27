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
