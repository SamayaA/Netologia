CREATE TABLE Genre (
id serial primary key , 
title varchar(50) not null unique
);
CREATE TABLE Performer (
id serial primary key, 
name varchar(50) not null
);
create table Genre_to_Performer (
genreId integer references Genre(id) ,
performerId integer references Performer(id) , 
constraint pk_PerformerGenre primary key ( genreId , performerId)
);
CREATE TABLE Album (
id serial primary key, 
title varchar(50) not null , 
release_date integer 
);

CREATE TABLE Album_to_Performer (
albumId integer references Album(id) ,
performerId integer references Performer(id) ,
constraint pk_AlbumPerformer primary key (albumId , performerId)
);

CREATE TABLE Track (
id serial primary key, 
title varchar(80) not null , 
duration numeric ,
albumid integer references Album(id)
);

CREATE TABLE Collection (
id serial primary key , 
name varchar (50) not null,
release_date integer
);

CREATE TABLE Track_to_collection (
trackid integer references Track(id) ,
collectionid integer references Collection(id),
constraint pk_TrackCollection primary key(trackid , collectionid)
);

--insert INTO genre    
--VALUES(1, 'Rock');
--INSERT INTO genre    
--VALUES(2, 'Jazz');
--
--insert INTO performer    
--VALUES(1, 'Anton');
--INSERT INTO Genre_to_Performer    
--VALUES(1, 1);
--INSERT INTO Genre_to_Performer    
--VALUES(2, 1);
--
--select performer.id , performer.name , genre.title from performer, genre , genre_to_performer
--where performer.id = genre_to_performer.performerid and genre.id = genre_to_performer.genreid ;

--drop table album , album_to_performer , genre , genre_to_performer ,performer , track , track_to_album , track_to_collection , collection ;