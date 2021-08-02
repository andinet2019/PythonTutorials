import psycopg2
conn= psycopg2.connect(database="and_database" ,user="postgres", password="Kangher115!",host="localhost",port="5432")
cur=conn.cursor()
cur.execute("""
CREATE TABLE stores_new
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);
""")
print("Table is created")
conn.commit()
conn.close()