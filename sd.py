import sqlite3
conn=sqlite3.connect("c2.db")
c=conn.cursor()

c.execute("""CREATE TABLE C5(NAME TEXT,ADDRESS TEXT,MOBILE TEXT,EMAIL TEXT,PASSWORD TEXT)""")
conn.commit()
conn.close()
