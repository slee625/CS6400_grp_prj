import psycopg2

conn = psycopg2.connect("dbname=RecipeBookDB user=postgres password=FloNAt8? host=localhost")

cur = conn.cursor()

cur.execute("SELECT * from recipes")
rows = cur.fetchall()

print(rows)

cur.close()
conn.close()