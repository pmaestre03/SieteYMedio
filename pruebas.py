import pymysql
conn=pymysql.connect(host="51.145.227.94",user="prius",password="P@ssw0rd",db="proyecto")
cur = conn.cursor()
query = f"select * from cards"
cur.execute(query)
variable = cur.fetchall()