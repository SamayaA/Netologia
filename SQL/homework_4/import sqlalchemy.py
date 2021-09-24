import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://user:password@localhost:5432/site')
engine
connection = engine.connect()
connection.execute("""
INSERT INTO genre(title) 
VALUES ('Pop'),
('Rock'),
('Country'),
('Soul'),
('Dance');""")

connection.execute("""
INSERT INTO performer(name) 
VALUES ('Alex'),
('Jhon'),
('Joe'),
('Amanda'),
('Loren'),
('One Republic'),
('Emre'),
('Coleen');""")

connection.execute("""
INSERT INTO album(title, release_date) 
VALUES ('Back in Black' , 2001 ),
('The Bodyguard' , 2008 ),
('Bat Out of Hell' , 2018 ),
('Their Greatest Hits (1971–1975)' , 2020 ),
('Dirty Dancing' , 2019 ),
('Millennium' , 2007 ),
('Saturday Night Fever' , 2018 ),
('Rumours' , 2019 );""")

connection.execute("""
INSERT INTO track(title, duration, albumid) 
VALUES ('Rolling In The Deep' , 2.5, 1),
('Chasing Cars' , 3.7, 2),
('I`m Gonna be' , 4.3, 3),
('Wheels' , 1.3, 4),
('Sail' , 1.8, 5),
('Auto Pilot' , 2.6, 6),
('On my Way' , 12.3, 7),
('Under Your Spell' , 4.7, 8),
('Tick Of The Clock' , 2.4, 1),
('Headlights' , 5.7, 2),
('Drive' , 2.0, 3),
('Walk On By' , 4.7, 4),
('Kicks' , 5.6, 5),
('Kickstart My Heart' , 3.7, 6),
('Fast Lane' , 5.2, 7 );""")

connection.execute("""
INSERT INTO collection(name, release_date) 
VALUES ('finnigan' , 2001 ),
('chevy' , 2008 ),
('mack' , 2018 ),
('miranda' , 2020 ),
('nasir' , 2019 ),
('eva' , 2007 ),
('reilly' , 2018 ),
('ajay' , 2019 );""")

connection.execute("""
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (3, 1),
(3, 2),
(6, 2),
(4, 3),
(5, 4),
(6, 5),
(7, 6),
(7, 4),
(5, 7);""")

connection.execute("""
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (2 , 1 ),
(2 , 2 ),
(1 , 3 ),
(3 , 4 ),
(4 , 5 ),
(5 , 6 ),
(6 , 7 ),
(7 , 8 ),
(8 , 5 ),
(6 , 2 );""")

connection.execute("""
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (1 , 1 ),
(2 , 2 ),
(3 , 3 ),
(4 , 4 ),
(5 , 5 ),
(6 , 6 ),
(7 , 7 ),
(8 , 8 ),
(9 , 1 ),
(10 , 2 ),
(11 , 3 ),
(12 , 4 ),
(13 , 5 ),
(14 , 6 ),
(15 , 7 );""")