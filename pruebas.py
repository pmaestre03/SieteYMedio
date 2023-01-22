import pymysql
import pymysql.cursors

conn=pymysql.connect(host="51.145.227.94",user="pmaestre",password="P@ssw0rd",db="proyecto")
# cur = conn.cursor()

update_players_in_game = conn.cursor()
select_game_bbdd = conn.cursor()
query_select_game_bbdd = f"set @id := (select max(id_game) from games)"
select_game_bbdd.execute(query_select_game_bbdd)
conn.commit()
query_update_players_in_game = f"update scores set Profits = Profits+10, total_games_played = total_games_played+1, minutes_pleyed = minutes_pleyed+(select (hour(TIMEDIFF(end_time,initial_time))*60+minute(TIMEDIFF(end_time,initial_time))) from games where id_game=23) where dni='13217155K'"
update_players_in_game.execute(query_update_players_in_game)
conn.commit()
