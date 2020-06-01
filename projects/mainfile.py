from room_select import room
from teach_select import teach
from compute import calculate
# from code import code
import sqlite3
import sys



class mainprog:
    def mainp(self,period,time,days):
        per = 1
        for day in range(int(days)):
              for per in range(int(period)):
                  conn = sqlite3.connect('data.sqlite')
                  # r1 = room()
                  # str=room.make1(r1)

                  str = "0"  # hexadecimal
                  print("str:", str)
                  m = calculate()
                  y = calculate.make(m, str)

                  print("y", y)
                  r2 = room()
                  x = room.make(r2, y)

                  # c = conn.cursor()
                  # c.execute('select code from data2 where class =?', str(x[0]))
                  # conn.commit()
                  #
                  print("x", x)
                  # aa = code(x)
                  # print("aa", aa)

                  t = teach()
                  teach.make(t, x,int(time))
                  # print(t1[0])

                  c = conn.cursor()
                  c.execute('select * from data2 where active =?', "1")
                  conn.commit()
                  print("aaa", c)
                  for qr in c:
                      out = conn.cursor()
                      out.execute('INSERT INTO outdata (period,room_id,teach_id,n_teach,sub_id,day) VALUES (?,?,?,?,?,?)',(per + 1, qr[2], qr[1], qr[3],qr[8],day+1))
                      conn.commit()
                  conn.close()


#print(sys.argv[1])
period=sys.argv[1]
time=sys.argv[2]
days=sys.argv[3]
x = mainprog()
y = mainprog.mainp(x,period,time,days)
