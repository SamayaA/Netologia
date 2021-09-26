select  genre.title , count(*) from genre , genre_to_performer gtp
where genre.id = gtp.genreid 
group by genre.title ;