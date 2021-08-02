import psycopg2
conn= psycopg2.connect(database="suppliers" ,user="postgres", password="Kangher115!",host="localhost",port="5432")
cur=conn.cursor()
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES(1,'Paul',32,'California',2000.0)");
cur.execute("INSERT INTO COMPANY( ID,NAME,AGE,ADDRESS,SALARY)  \
    VALUES(2, 'Zene',34,'Peru', 3000.0)");
cur.execute("INSERT INTO COMPANY( ID,NAME,AGE,ADDRESS,SALARY)  \
    VALUES(3, 'Zen',39,'Madlin', 300)");
cur.execute("INSERT INTO COMPANY( ID,NAME,AGE,ADDRESS,SALARY)  \
    VALUES(4, 'Paku',20,'Germany', 200.0)");
conn.commit()
conn.close()
