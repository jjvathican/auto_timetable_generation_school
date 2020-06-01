import sqlite3
conn = sqlite3.connect('data.sqlite')
c = conn.cursor()
#c.execute("INSERT INTO login VALUES ('jerin','pass')")
c.execute("ALTER TABLE data2  autoincrement")

conn.commit()
conn.close()
