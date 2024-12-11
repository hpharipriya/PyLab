import psycopg2
import requests
db_params = {
    'dbname': 'name',
    'user': 'user',
    'password': '',
    'host': 'host',
    'port': 5432
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

query = "select * from articles where path::text ~ '\.' order by id "

cursor.execute(query)

results = cursor.fetchall()
for result in results:
    print(result)
