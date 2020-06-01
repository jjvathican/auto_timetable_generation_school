import sqlite3
from htmlfile import viewrom
def view():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from room')
    conn.commit()
    viewrom(c)
    conn.close()
view()
