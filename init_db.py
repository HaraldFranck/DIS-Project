import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="movies",
        user=os.environ['magnus'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS movies;')
cur.execute('CREATE TABLE movies (title varchar (150),'
                                 'year integer NOT NULL,'
                                 'certificate varchar (10),'
                                 'runtime integer,'
                                 'genres varchar (150),'
                                 'rating real,'
                                 'overview varchar (300),'
                                 'metascore integer,'
                                 'director varchar (50),'
                                 'gross varchar (30)',
                                'PRIMARY KEY (title, year));'
                                 )
cur.execute('DROP TABLE IF EXISTS acts_in;')
cur.execute('CREATE TABLE acts_in (actor varchar (40) PRIMARY KEY,'
                                'movie varchar (150),'
                                'year integer,'
                                'FOREIGN KEY (movie) REFERENCES movies(title),'
                                'FOREIGN KEY (year) REFERENCES movies(year));')

conn.commit()

cur.close()
conn.close()
