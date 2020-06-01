import sqlite3
import rsort2


# c.execute("SELECT count(*)  FROM login WHERE user=? AND pass=?", (username, password))
# state= len(c.fetchall());
# state = c.fetchone()
# print(state[0])
#
# if (state[0] == 1):
#     tm.showinfo("Login info", "Welcome ")


class room:

    def __init__(self):

        self.ar = []


    def make(self,a):

        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()
        c.execute('select room_id from data2 group by room_id')
        t = c
        # print(ar)
        # print(t.fetchall())
        co = 0
        br=[]
        for j in t:
          sum=0
          m = a % 10
          if (m == 0 ):
            print('room',j)
            # ar[j] = j
            br=br+[j[0]]
            print("br",br)
            c = conn.cursor()
            c.execute('select hour from data2 where  room_id=? ', str(j[0]))
            conn.commit()
            # print(c)
            for i in c:
                # print("i",i[0])
                sum = sum + i[0]
          print(sum)
          self.ar = self.ar + [sum]
          co = co + 1
          a = int(a / 10)
        #print("ar", self.ar)
        #print("b", b)
        self.ar,b = rsort2.radixsort(self.ar,br)
        # print("ar", self.ar)
        # print("b", b)
        self.ar.reverse()
        b.reverse()
        print("ar", self.ar)
        print("b", b)
        # for n in range(len(self.ar)):
        #     if (self.ar[n] == 0):
        #         b[n] = 0

        # print("ar", self.ar)
        # print("b",b)

        conn.close()
        return b



    def make1(self):

         conn = sqlite3.connect('data.sqlite')
         c = conn.cursor()
         c.execute('select room_id from data2 group by room_id')
         conn.commit()
         t = c
         co = 0
         for j in t:
             print('room', j)
             sum = 0
             # ar[j] = j
             c = conn.cursor()
             c.execute('select hour from data2 where  room_id=? ', str(j[0]))
             conn.commit()

             print("c",c)
             for i in c:
                 print(i[0])
                 sum = sum + i[0]
             print(sum)
             self.ar = self.ar + [sum]
             co = co + 1

         self.ar, b = rsort2.radixsort(self.ar)
         self.ar.reverse()
         b.reverse()
         print("ar",self.ar)
         print("b:",b)
         c = conn.cursor()
         c.execute('select max(hour),code,n_id from data2 where room_id= ? ', str(b[0]))
         conn.commit()
         l = c.fetchone()
         print("l:",l)

         conn.close()
         return l[1]




# x=room()
# y=room.make(x,0)
# print(y)
# # #

