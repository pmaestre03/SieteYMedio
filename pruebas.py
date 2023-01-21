import pymysql
import pymysql.cursors

conn=pymysql.connect(host="51.145.227.94",user="pmaestre",password="P@ssw0rd",db="proyecto")
# cur = conn.cursor()

update_game_in_bbdd = conn.cursor()
select_game_bbdd = conn.cursor()
query_select_game_bbdd = f"set @id := (select max(id_game) from games)"
select_game_bbdd.execute(query_select_game_bbdd)
conn.commit()
query_end_game_bbdd = f"update games set end_time = (select sysdate()) where id_game = @id"
update_game_in_bbdd.execute(query_end_game_bbdd)
conn.commit()