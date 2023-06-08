import psycopg2
import csv 

conn = psycopg2.connect(
        host="localhost",
        database="movies",
        user='postgres',
        password='passwor')

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS movies CASCADE;')
cur.execute('CREATE TABLE movies (title varchar (150),'
                                 'year integer NOT NULL,'
                                 'certificate varchar (10),'
                                 'runtime integer,'
                                 'genres varchar (150),'
                                 'rating real,'
                                 'overview varchar (500),'
                                 'metascore integer,'
                                 'director varchar (50),'
                                 'gross varchar (30),'
                                'PRIMARY KEY (title, year));'
                                 )
cur.execute('DROP TABLE IF EXISTS acts_in CASCADE;')
cur.execute('CREATE TABLE acts_in (actor varchar (40),'
                                'movie varchar (150),'
                                'year integer,'
                                'FOREIGN KEY (movie, year) REFERENCES movies (title,year));')

with open('imdb_top_1000.csv', 'r', encoding="UTF-8") as f:
    reader = csv.reader(f, )
    next(reader) # Skip the header row.
    for row in reader:
        runtime = row[4][:2]
        if row[8] == '':
            metascore = 0
        else:
            metascore = row[8]
        cur.execute(
        "INSERT INTO movies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        (row[1], row[2], row[3], runtime, row[5], row[6], 
        row[7], metascore, row[9], row[15]))

with open('imdb_top_1000.csv', 'r', encoding="UTF-8") as f:
    reader = csv.reader(f, )
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO acts_in VALUES (%s, %s, %s)", 
        (row[10], row[1], row[2]))
        cur.execute(
        "INSERT INTO acts_in VALUES (%s, %s, %s)", 
        (row[11], row[1], row[2]))
        cur.execute(
        "INSERT INTO acts_in VALUES (%s, %s, %s)", 
        (row[12], row[1], row[2]))
        cur.execute(
        "INSERT INTO acts_in VALUES (%s, %s, %s)", 
        (row[13], row[1], row[2]))


conn.commit()

cur.close()
conn.close()
