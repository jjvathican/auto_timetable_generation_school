from compute import calculate
from room_select import room
from hehe import seek
from addd import sumit
from he1 import a_ar
from random import randint
import sqlite3


def code(time):
    # print("code")
    st = "0"  # hexadecimal
    print("str:", st)
    m = calculate()
    y = calculate.make(m, st)

    print("y", y)
    r2 = room()
    x = room.make(r2, y)
    conn = sqlite3.connect('data.sqlite')
    te = []
    id = []
    nd = []
    for i in x:
        c = conn.cursor()
        c.execute('select code,teach_id,n_id from data2 where room_id= ?', (str(i),))
        conn.commit()
        r = []
        d = []
        n = []
        for j in c:
            print("j",j)
            a = j[0]
            m = calculate()
            y = calculate.make(m, a)
            r = r + [y]
            d = d + [j[1]]
            n = n + [j[2]]
        # print(r)
        te = te + [r]
        id = id + [d]
        nd = nd + [n]

    print(te)
    print("id",id)
    print(nd)
    cal=len(x)*(len(max(id))*2)
    sr = seek(id,cal)
    print("sr",sr)
    sid_ar=[]
    for ar in sr:
          print("ar", ar)
          # co=[i for i in range(len(ar))]
          n_tea = []

          for aa in range(len(ar)):
              c = conn.cursor()
              c.execute('select max(n_teach) from data2 where room_id= ? and teach_id=?', (str(x[aa]), str(ar[aa]),))
              conn.commit()
              l = c.fetchone()
              n_tea = n_tea + [l[0]]

          co = []
          no = []
          for aa in range(len(ar)):
              c = conn.cursor()
              c.execute('select code,n_id from data2 where room_id= ? and teach_id=? and n_teach=?',(str(x[aa]), str(ar[aa]), str(randint(1,n_tea[aa])),))
              conn.commit()
              for j in c:
                  bb = j[0]
                  m = calculate()
                  y = calculate.make(m, bb)
                  co = co + [y]
                  no = no + [j[1]]
          print("co", co)
          print("no", no)
          sum = sumit(co)
          print("sum", sum)
          print("x", x)
          sclass = []
          for i in x:
              try:
                  if (sum[i - 1] == 0):
                      sclass = sclass + [i]
              except:
                  sclass = sclass + [i]
          sid = []
          for i in range(len(x)):
              if (a_ar(sclass, x[i]) == 1):#searching for x[i] in sclass , returns 1 if found
                  sid = sid + [no[i]]
          # try:
          #
          # except:
          #     sid = sid + []
          print("sclass", sclass)
          print("sid", sid)
          sid_ar=sid_ar+[sid]
    list = [x for x in sid_ar if x != []]#to remove empty array
    for s in list:
        for nid in s:
          c = conn.cursor()
          c.execute('select hour from data2 where n_id = ?',(str(nid),))
          l = c.fetchone()
          conn.commit()
          h = l[0]
          c = conn.cursor()
          c.execute('UPDATE data2 SET hour =? , active =? WHERE  n_id = ?', (str(h-time), "1", str(nid),))
          conn.commit()
    conn.close()

    return list



y = code(60)
print("y", y)




# while(a>0):
#     b=a%10
#     r=[[0 for t in range()]]
#     a=a/10
# ar=[]
#
#
# for i in id:
#
#     for u in range(len(ar)):
#         if (ar[u] == id[i][r]):
#             break
#     r=random.randint(0, len(id[0]))
#     print(r)


# ar = []
# u = 0
# q = 0
# count = 0
# # print(0%len(id[0]))
# print(id[0][0])
# # ar=ar+[id[0][0]]
#
# print("a", a)
# print("id", len(id[i]))
# q = -1
# for u in range(len(ar)):
#     print("hai")
#     print(ar[u], id[i][a])
#     if (ar[u] == id[i][a]):
#         break
#     q = u
# print("q", q)
# print("ar", ar)
# if (q == len(ar) - 1):
#     print("add")
#     ar = ar + [id[i][a]]
# print("q", q)
# print("ar", ar)

#
# count = count + 1
# ar=[]
# for ii in range(len(id)):
#     for jj in range(len(id[0      ])):

# ar=[]
# u=0
# count=[0 for i in range(len(id))]
# for i in range(len(id)):
#     while (u == len(ar)-1):
#         for u in range(len(ar)):
#             if (ar[u] == id[i][a]):
#                 break
#         a = count[i] % len(id[i])
#         count[i]=count[i]+1
#     ar=ar+[id[i][a]]


# print(ar)
