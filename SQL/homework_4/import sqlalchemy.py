import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://...@localhost:5432/site')
engine
connection = engine.connect()
connection.execute("""
INSERT INTO genre(title) 
VALUES ('Pop');
INSERT INTO genre(title) 
VALUES ('Rock');
INSERT INTO genre(title) 
VALUES ('Country');
INSERT INTO genre(title) 
VALUES ('Soul');
INSERT INTO genre(title) 
VALUES ('Dance');""")

connection.execute("""
INSERT INTO performer(name) 
VALUES ('Alex');
INSERT INTO performer(name) 
VALUES ('Jhon');
INSERT INTO performer(name) 
VALUES ('Joe');
INSERT INTO performer(name) 
VALUES ('Amanda');
INSERT INTO performer(name) 
VALUES ('Loren');
INSERT INTO performer(name) 
VALUES ('One Republic');
INSERT INTO performer(name) 
VALUES ('Emre');
INSERT INTO performer(name) 
VALUES ('Coleen');""")

connection.execute("""
INSERT INTO album(title, release_date) 
VALUES ('Back in Black' , 2001 );
INSERT INTO album(title, release_date) 
VALUES ('The Bodyguard' , 2008 );
INSERT INTO album(title, release_date) 
VALUES ('Bat Out of Hell' , 2018 );
INSERT INTO album(title, release_date) 
VALUES ('Their Greatest Hits (1971–1975)' , 2020 );
INSERT INTO album(title, release_date) 
VALUES ('Dirty Dancing' , 2019 );
INSERT INTO album(title, release_date) 
VALUES ('Millennium' , 2007 );
INSERT INTO album(title, release_date) 
VALUES ('Saturday Night Fever' , 2018 );
INSERT INTO album(title, release_date) 
VALUES ('Rumours' , 2019 );""")

connection.execute("""
INSERT INTO track(title, duration) 
VALUES ('Rolling In The Deep' , 2.5 );
INSERT INTO track(title, duration) 
VALUES ('Chasing Cars' , 3.7 );
INSERT INTO track(title, duration) 
VALUES ('I`m Gonna be' , 4.3 );
INSERT INTO track(title, duration) 
VALUES ('Wheels' , 1.3 );
INSERT INTO track(title, duration) 
VALUES ('Sail' , 1.8 );
INSERT INTO track(title, duration) 
VALUES ('Auto Pilot' , 2.6 );
INSERT INTO track(title, duration) 
VALUES ('On my Way' , 12.3 );
INSERT INTO track(title, duration) 
VALUES ('Under Your Spell' , 4.7 );
INSERT INTO track(title, duration) 
VALUES ('Tick Of The Clock' , 2.4 );
INSERT INTO track(title, duration) 
VALUES ('Headlights' , 5.7 );
INSERT INTO track(title, duration) 
VALUES ('Drive' , 2.0 );
INSERT INTO track(title, duration) 
VALUES ('Walk On By' , 4.7 );
INSERT INTO track(title, duration) 
VALUES ('Kicks' , 5.6 );
INSERT INTO track(title, duration) 
VALUES ('Kickstart My Heart' , 3.7 );
INSERT INTO track(title, duration) 
VALUES ('Fast Lane' , 5.2 );""")

connection.execute("""
INSERT INTO collection(name, release_date) 
VALUES ('finnigan' , 2001 );
INSERT INTO collection(name, release_date) 
VALUES ('chevy' , 2008 );
INSERT INTO collection(name, release_date) 
VALUES ('mack' , 2018 );
INSERT INTO collection(name, release_date)  
VALUES ('miranda' , 2020 );
INSERT INTO collection(name, release_date) 
VALUES ('nasir' , 2019 );
INSERT INTO collection(name, release_date) 
VALUES ('eva' , 2007 );
INSERT INTO collection(name, release_date) 
VALUES ('reilly' , 2018 );
INSERT INTO collection(name, release_date) 
VALUES ('ajay' , 2019 );""")

connection.execute("""
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (3, 1);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (3, 2);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (6, 2);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (4, 3);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (5, 4);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (6, 5);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (7, 6);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (7, 4);
INSERT INTO genre_to_performer(genreid , performerid) 
VALUES (5, 7);""")

connection.execute("""
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (2 , 1 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (2 , 2 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (1 , 3 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (3 , 4 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (4 , 5 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (5 , 6 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (6 , 7 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (7 , 8 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (8 , 5 );
INSERT INTO album_to_performer(albumid, performerid) 
VALUES (6 , 2 );""")

connection.execute("""
INSERT INTO track_to_album(trackid, albumid) 
VALUES (1 , 1 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (2 , 2 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (3 , 3 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (4 , 4 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (5 , 5 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (6 , 6 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (7 , 7 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (8 , 8 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (9 , 1 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (10 , 2 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (11 , 3 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (12 , 4 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (13 , 5 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (14 , 6 );
INSERT INTO track_to_album(trackid, albumid) 
VALUES (15 , 7 );""")

connection.execute("""
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (1 , 1 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (2 , 2 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (3 , 3 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (4 , 4 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (5 , 5 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (6 , 6 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (7 , 7 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (8 , 8 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (9 , 1 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (10 , 2 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (11 , 3 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (12 , 4 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (13 , 5 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (14 , 6 );
INSERT INTO track_to_collection(trackid, collectionid) 
VALUES (15 , 7 );""")