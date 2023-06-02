from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='movies',
                            user='postgres',
                            password='passwor')
    return conn

@app.route('/')
def index():
    return render_template('search_form.html')


@app.route('/search', methods=['POST'])
def search_movies():
    # Retrieve the search criteria from the request
    title = request.form.get('title')
    actor = request.form.get('actor')
    genre = request.form.get('genre')
    director = request.form.get('director')

    # Set up a database connection
    conn =  get_db_connection()
    cursor = conn.cursor()

    try:
        # Construct the SQL query based on the search criteria
        query = "SELECT movies.title, movies.year, movies.genres, movies.director FROM movies"

        # Join acts_in table to fetch movies where the specified actor is involved
        if actor:
            query += " INNER JOIN acts_in ON movies.title = acts_in.movie AND movies.year = acts_in.year"

        conditions = []
        values = []

        if title:
            conditions.append("movies.title ILIKE %s")
            values.append(f"%{title}%")
        if actor:
            conditions.append("acts_in.actor = %s")
            values.append(actor)
        if genre:
            conditions.append("movies.genres ILIKE %s")
            values.append(f"%{genre}%")
        if director:
            conditions.append("movies.director = %s")
            values.append(director)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Execute the query
        cursor.execute(query, values)
        movies = cursor.fetchall()
        return render_template('search_results.html', movies=movies)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
    