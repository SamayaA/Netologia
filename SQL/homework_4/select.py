import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://...@localhost:5432/site')
engine
connection = engine.connect()
show = connection.execute("""
SELECT title , release_date FROM album
WHERE release_date=2018 ;
""").fetchall()
print(show)
show = connection.execute("""
SELECT title , duration FROM track
ORDER BY duration DESC
LIMIT 1 ;
""").fetchall()
print(show)
show = connection.execute("""
SELECT title FROM track
WHERE duration >=3.5 ;
""").fetchall()
print(show)
show = connection.execute("""
SELECT name FROM collection
WHERE release_date BETWEEN 2018 AND 2020 ;
""").fetchall()
print(show)
show = connection.execute("""
SELECT name FROM performer
WHERE name NOT LIKE '%% %%' ;
""").fetchall()
print(show)
show = connection.execute("""
SELECT title FROM track
WHERE title LIKE'%%мой%%' OR title LIKE '%%my%%' ;
""").fetchall()
print(show)