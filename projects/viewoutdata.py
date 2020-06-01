import sqlite3
from htmlfile import viewout
def view():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from outdata')
    conn.commit()
    viewout(c)
    conn.close()
view()
