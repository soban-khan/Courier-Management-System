import sqlite3
conn=sqlite3.connect("Pizza.db")
c=conn.cursor()
c.execute("""CREATE TABLE PIZZA2(NAME TEXT,ADDRESS TEXT,SMALL REAL,MEDIUM REAL,LARGE REAL,MOBILE TEXT,EMAIL TEXT)""")
conn.commit()
conn.close()
