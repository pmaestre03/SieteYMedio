import pymysql
conn=pymysql.connect(host="51.145.227.94",user="pmaestre",password="P@ssw0rd",db="proyecto")
cur = conn.cursor()

prop2 = conn.cursor()
queryprop2 = f"select g.id_game,gp.dni,r.points_bet from games g inner join game_player gp on g.id_game = gp.id_game inner join round r on gp.dni = r.dni where r.points_bet = (select max(r.points_bet) from round)"
prop2.execute(queryprop2)
propuesta2 = list(prop2.fetchall())
print(propuesta2)


prop3 = conn.cursor()
queryprop3 = f"select g.id_game,gp.dni,r.points_bet from games g inner join game_player gp on g.id_game = gp.id_game inner join round r on gp.dni = r.dni where r.points_bet = (select min(r.points_bet)from round);"
prop3.execute(queryprop3)
propuesta3 = prop3.fetchall()
print(propuesta3)

prop5 = conn.cursor()
queryprop5 = f"select w.id_game,w.points from winners w inner join player p on w.dni = p.dni where p.human = 0;"
prop5.execute(queryprop5)
propuesta5 = prop5.fetchall()
print(propuesta5)

prop7 = conn.cursor()
queryprop7 = f"select g.id_game,count(distinct dni) as banca from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round where r.bank = 1 group by g.id_game;"
prop7.execute(queryprop7)
propuesta7 = list(prop7.fetchall())
print(propuesta7)

prop8 = conn.cursor()
queryprop8 = f"select g.id_game,avg(r.points_bet) as media_puntos_partida from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round group by rg.id_game;"
prop8.execute(queryprop8)
propuesta8 = prop8.fetchall()
print(propuesta8)

prop9 = conn.cursor()
queryprop9 = f"select g.id_game,avg(r.points_bet) as media from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round where rg.id_round = 1 group by rg.id_round_games;"
prop9.execute(queryprop9)
propuesta9 = prop9.fetchall()
print(propuesta9)

prop10 = conn.cursor()
queryprop10 = f"select g.id_game,avg(r.points_bet) as media_ultima_ronda from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round where rg.id_round = (select max(rg.id_round) from round_games) group by rg.id_round_games;"
prop10.execute(queryprop10)
propuesta10 = prop10.fetchall()
print(propuesta10)

prop7 = conn.cursor()
queryprop8 = f"select g.id_game,avg(r.points_bet) as media_puntos_partida from games g inner join round_games rg on g.id_game = rg.id_game inner join round r on rg.id_round = r.id_round group by rg.id_game;"
prop8.execute(queryprop8)
propuesta8 = list(prop8.fetchall())
print(propuesta8)
