import sqlite3

d = { "id" : "P0003",
      "title" : "Node.js程式設計",
      "price" : 650 }

book = "P0002, Python程式設計, 500"
f = book.split(",")

conn = sqlite3.connect("books.sqlite")

# sql = "insert into books (id, title, price) values('{0}', '{1}', '{2}')"
# sql=sql.format(d["id"], d["title"], d["price"])
# print (sql)

# sql2 = "insert into books (id, title, price) values('{0}', '{1}', '{2}')"
# sql2=sql2.format(f[0], f[1], f[2])
# print (sql2)

# cursor = conn.execute(sql2)
# print (cursor.rowcount)


cur2 = conn.execute("select * from books")

for row in cur2 :
    print ("id :",row[0])
    print ("title :",row[1])
    print ("price :",row[2], "\n")
    
print ("Operation done successfully !")

conn.commit()
conn.close()
