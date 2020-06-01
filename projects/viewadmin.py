import sqlite3
from htmlfile import viewad
def view():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from admin')
    conn.commit()
    viewad(c)
    conn.close()
view()
