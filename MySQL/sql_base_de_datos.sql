use proyecto;
drop table if exists cards_round;
drop table if exists round_games;
drop table if exists round;
drop table if exists game_player;
drop table if exists scores;
drop table if exists player;
drop table if exists games;
drop table if exists cards;
drop table if exists winners;

create table if not exists player(
dni varchar(9) unique not null  primary key,
name varchar(25) not null,
level_risc int not null,
human boolean not null);

create table if not exists cards(
id_card varchar(3) not null unique primary key,
type_deck varchar(20) not null,
value_in_game float not null,
cards_true_value int not null,
deck_suits varchar(25) not null);

create table if not exists games(
id_game int not null unique auto_increment primary key,
initial_time timestamp null,
end_time timestamp null,
n_players int not null,
n_round int not null,
type_deck varchar(25) not null);

create table if not exists  game_player(
id_game_player int not null unique auto_increment primary key,
dni varchar(9) not null,
id_game int not null,
constraint fk_gp_g foreign key (dni) 
references player(dni),
constraint fk_gp_p foreign key(id_game)
references games(id_game));

savepoint s1;

create table if not exists round(
id_round int not null auto_increment primary key,
round_game int not null,
dni varchar(9) not null,
bank boolean not null,
point_begin int not null,
point_end int not null,
points_bet int not null,
constraint fk_r_p foreign key (dni) 
references player(dni));

create table if not exists cards_round(
id_cards_round int not null unique auto_increment primary key,
dni varchar(9) not null,
id_card varchar(3) not null,
id_round int not null,
id_game int not null,
n_card_round int not null,
decks_suits varchar(25) not null,
constraint fk_cr_p foreign key (dni) 
references player(dni),
constraint fk_cr_r foreign key (id_round) 
references round(id_round),
constraint fk_cr_g foreign key (id_game) 
references games(id_game),
constraint fk_cr_c
    foreign key (id_card)
    references cards (id_card)
);

create table if not exists round_games(
id_round_games int not null unique auto_increment primary key,
id_round int not null,
id_game int not null,
constraint fk_rg_r foreign key (id_round) 
references round(id_round),
constraint fk_rg_g foreign key (id_game) 
references games(id_game));

create table if not exists scores(
id_score int not null unique auto_increment primary key,
dni varchar(9) not null,
Profits int not null,
total_games_played int not null,
minutes_pleyed int not null,
constraint fk_p_s foreign key (dni) 
references player(dni));

create table if not exists winners(
id_game int not null primary key,
dni varchar(9) not null,
points int not null
);

savepoint s2;

insert into player (dni,name,level_risc,human)
values('38980142H','jose',30,True);
insert into player (dni,name,level_risc,human)
values('32314124K','carlos',40,false);
insert into player (dni,name,level_risc,human)
values('66903220S','marcos',50,false);
