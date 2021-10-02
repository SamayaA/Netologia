-- 1. count performer by genre
SELECT  title , COUNT(gtp.genreid) FROM genre
JOIN genre_to_performer gtp ON genre.id = gtp.genreid 
GROUP BY genre.title ;
-- 2. count tracks which belongs to albums released in (2019 - 2020)
SELECT COUNT(albumid) FROM album a
JOIN track t ON t.albumid = a.id
WHERE a.release_date BETWEEN 2019 and 2020;
-- 3. avg duration of tracks by album
SELECT a.title , AVG(t.duration) FROM album a
LEFT JOIN track t ON t.albumid = a.id 
GROUP BY a.title ;
-- 4. performers didn't release albums in 2020
SELECT performer.name FROM performer 
WHERE performer.id NOT IN (
	SELECT performerid FROM album a 
	LEFT JOIN album_to_performer atp ON a.id = atp.albumid 
	WHERE a.release_date = 2020);

-- 5. collections of certain performer
SELECT DISTINCT collection.name FROM collection 
LEFT JOIN track_to_collection ttc ON collection.id = ttc.collectionid
LEFT JOIN track t ON t.id = ttc.trackid
FULL JOIN album_to_performer atp ON t.albumid = atp.albumid
WHERE atp.performerid = 2;
-- 6. albums written by performer of different genres
SELECT distinct album.title FROM album
JOIN album_to_performer atp ON atp.albumid = album.id
JOIN genre_to_performer gtp ON gtp.performerid = atp.performerid
GROUP BY album.title
HAVING COUNT(gtp.performerid)>1;
-- 7. tracks that not included in collections
SELECT track.title FROM track
WHERE track.id NOT IN (
    SELECT DISTINCT trackid FROM track_to_collection);
-- 8. performers with shortest tracks
SELECT p.name FROM performer p
JOIN album_to_performer atp ON p.id = atp.performerid
RIGHT JOIN track t ON atp.albumid= t.albumid 
	WHERE duration = (SELECT MIN(duration) FROM track)
;
-- 9. albums with least amount tracks
SELECT DISTINCT album.title FROM album , track 
WHERE album.id = (
	SELECT albumid FROM (
		SELECT distinct albumid , count(track.albumid) FROM track 
		GROUP BY albumid
		ORDER BY count(track.albumid) ASC
		LIMIT 1) as foo);


