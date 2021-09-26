-- count performer by genre
SELECT  genre.title , COUNT(*) FROM genre , genre_to_performer gtp
WHERE genre.id = gtp.genreid 
GROUP BY genre.title ;
-- count tracks which belongs to albums released in (2019 - 2020)
SELECT COUNT(*) FROM track t, album 
WHERE (album.release_date BETWEEN 2019 and 2020) and 
t.albumid = album.id ;
-- avg duration of tracks by album
SELECT album.title , AVG(track.duration) FROM album, track 
WHERE track.albumid = album.id 
GROUP BY album.title ;
-- performers didn't release albums in 2020
SELECT performer.name FROM performer 
WHERE performer.id NOT IN (
	SELECT performerid FROM album , album_to_performer atp 
	WHERE album.id = atp.albumid AND album.release_date = 2020);

-- collections of certain performer
SELECT DISTINCT collection.name FROM collection , track_to_collection ttc 
WHERE collection.id = ttc.collectionid AND ttc.trackid IN(
	SELECT track.id FROM track
	WHERE track.albumid IN (
		SELECT albumid FROM album_to_performer atp 
		WHERE performerid = 2));
-- albums written by performer of different genres
SELECT album.title FROM album
WHERE album.id IN (
	SELECT DISTINCT album_to_performer.albumid FROM album_to_performer , genre_to_performer gtp
	WHERE gtp.performerid = album_to_performer.performerid
	GROUP BY album_to_performer.albumid
	having COUNT(gtp.performerid)>1 
);
-- tracks that not included in collections
SELECT track.title FROM track
WHERE track.id NOT IN (
    SELECT DISTINCT trackid FROM track_to_collection);
-- performers with shortest tracks
SELECT performer.name FROM performer
WHERE performer.id in (
	SELECT DISTINCT performerid FROM album_to_performer atp
	WHERE albumid IN (
		SELECT albumid FROM track t 
		WHERE duration = (SELECT MIN(duration) FROM track))
	);
-- albums with least amount tracks
SELECT DISTINCT album.title FROM album , track 
WHERE album.id = (
	SELECT albumid FROM (
		SELECT distinct albumid , count(track.albumid) FROM track 
		GROUP BY albumid
		ORDER BY count(track.albumid) ASC
		LIMIT 1) as foo);


