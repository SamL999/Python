import sqlite3

conn = sqlite3.connect("test.sqlite")

cursor = conn.cursor()

sqlstr = "create table if not exists table01 ('num' integer primary key not null, 'tel' text)"
cursor.execute(sqlstr)

sqlstr = "insert into table01 values(4, '06-33564896')"
cursor.execute(sqlstr)

conn.commit()
conn.close()


