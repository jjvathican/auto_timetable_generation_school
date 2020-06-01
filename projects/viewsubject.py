import sqlite3
from htmlfile import viewsub
def view():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from subject ')
    conn.commit()
    viewsub(c)
    conn.close()
view()