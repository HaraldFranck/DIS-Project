import flask
import psycopg2


conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="your_port")
cursor = conn.cursor()

with open('path/to/csv/file.csv', 'r') as file:
    next(file)  # Skip the header row if it exists
    cursor.copy_from(file, 'table_name', sep=',')

conn.commit()
cursor.close()
conn.close()
