import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

class connectDb():
    def __init__(self, db="postgres", user="postgres", password="postgres", host='localhost'):
        self.conn = psycopg2.connect(database=db, user=user, password=password)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def fetch_all(self, query):
        self.cur.execute(query)
        self.conn.commit()
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()

db = connectDb(db='test', user='postgres')
print(db.query("INSERT INTO public.sales(amount)VALUES(%i);"%876))
rows = db.fetch_all("SELECT * FROM sales;")
print(type(rows))
db.close()

"""
con = psycopg2.connect(dbname='postgres',
      user='postgres', host='localhost',
      password='postgres')

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

def create_db(db_name):
    cur = con.cursor()
    try:
        rta = cur.execute("CREATE DATABASE %s;"%(db_name))
    except:
        rta = "Error"
    return rta

print(create_db("testa6"))
"""