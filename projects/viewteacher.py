import sqlite3
from htmlfile import viewtea
def view():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from teacher ')
    conn.commit()
    viewtea(c)
    conn.close()
view()