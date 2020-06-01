import sqlite3
conn = sqlite3.connect('data.sqlite')
c = conn.cursor()
#c.execute("CREATE TABLE login(id integer primary key autoincrement not null,user text not null, PASS text not null)")
#c.execute("INSERT INTO login (user,pass)VALUES ('jerin','pass')")
c.execute("select * from data1 ")
l=c.fetchall()
print(l)
conn.commit()
conn.close()

