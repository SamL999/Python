import sqlite3

conn = sqlite3.connect("test.sqlite")

cursor = conn.execute("select * from table01")

# print(cursor)

# rows = cursor.fetchall()
# print (rows)

# for row in rows :
#     print ("{:d} \t {:s}".format(row[0],row[1]))

for row in cursor :
    print (row)

conn.close()
