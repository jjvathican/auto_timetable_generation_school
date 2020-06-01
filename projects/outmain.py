import sqlite3
import sys
from htmlfile import htmlc,htmlt
def outclass(cid):
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from outdata where room_id =?', str(cid))
    conn.commit()
    ht=[]
    for i in c:
       d = conn.cursor()
       d.execute('select r_name from room where room_id =?',str(i[2]))
       conn.commit()
       l1=d.fetchone()
       e = conn.cursor()
       e.execute('select t_name from teacher where teach_id =?',str(i[3]))
       l2=e.fetchone()
       conn.commit()
       e.execute('select s_name from subject where sub_id =?', str(i[5]))
       l3 = e.fetchone()
       conn.commit()
       ht=ht+[[i[1],l1[0],l2[0],l3[0]]]

    conn.close()
    print(ht)
    htmlc(ht)
def outteacher(cid):
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('select * from outdata where teach_id =?', str(cid))
    conn.commit()
    ht = []
    for i in c:
        d = conn.cursor()
        d.execute('select r_name from room where room_id =?', str(i[2]))
        conn.commit()
        l1 = d.fetchone()
        e = conn.cursor()
        e.execute('select t_name from teacher where teach_id =?', str(i[3]))
        l2 = e.fetchone()
        conn.commit()
        e.execute('select s_name from subject where sub_id =?', str(i[5]))
        l3 = e.fetchone()
        conn.commit()
        ht = ht + [[i[1], l1[0], l2[0], l3[0]]]

    conn.close()
    print(ht)
    htmlt(ht)

# conn = sqlite3.connect('data.sqlite')
# c = conn.cursor()
# c.execute('select max(teach_id) from outdata')
# conn.commit()
#
# conn.close()
outclass(sys.argv[1])
outteacher(1)