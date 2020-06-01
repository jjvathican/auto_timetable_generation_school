#from room_select import room
import sqlite3


class teach:
    def   make(self,x,time):

        # print(self.x)
        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()
        c.execute('UPDATE data2 SET active =? ',"0")
        conn.commit()
        c = conn.cursor()
        c.execute('UPDATE data2 SET t_active =? ', "0")
        conn.commit()
        for i in x:
            try:
                print(i)
                c = conn.cursor()
                c.execute('select max(hour),n_id,teach_id from data2 where room_id= ? and active= ? and t_active= ?',( str(i),"0","0"))
                l = c.fetchone()
                conn.commit()
                print(l, "hi")
                h = l[0]
                n_id = l[1]
                teach_id=l[2]

                c = conn.cursor()
                c.execute('UPDATE data2 SET hour =? , active =? WHERE  n_id = ?', (str(h - time),"1", str(n_id)))
                conn.commit()
                c = conn.cursor()
                c.execute('UPDATE data2 SET t_active =? WHERE  teach_id = ?', ("1", str(teach_id)))
                conn.commit()
            except:
               print("leaving")

        # print(l[1])
        #conn.commit()
        conn.close()


# x=[0,1]
# y = teach()
# y=teach.make(y,x)
