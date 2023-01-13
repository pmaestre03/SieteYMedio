import pymysql
conn=pymysql.connect(host="51.145.227.94",user="prius",password="P@ssw0rd",db="proyecto")
cur = conn.cursor()

query = f"select * from scores"
cur.execute(query)
scores = cur.fetchall()




print(scores)

var = list(scores)
for pasadas in range(len(var)-1):
        for comp in range(len(var)-1-pasadas):
            if var[comp][2] < var[comp+1][2]:
                var[comp],var[comp+1] = var[comp+1],var[comp]
for i in var:
    listaOrd = f'{i}'
    print(listaOrd)