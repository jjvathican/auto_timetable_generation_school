class fun1:
    def make(self, ar, le):
        ed = 10 ** le
        st = 10 ** (le - 1)
        print(st)
        count = 0
        for i in range(0, len(ar), +1):
            if (ar[i] < ed and ar[i] >= st):
                count = count + 1
        self.tem1 = [-1 for j in range(count)]
        count = 0
        for i in range(0, len(ar), +1):
            if (ar[i] < ed and ar[i] >= st):
                self.tem1[count] = ar[i]
                count = count + 1
        return self.tem1


class fun2:
    def make(self, x, le):
        t = [x[j] for j in range(len(x))]
        t1 = [x[j] for j in range(len(t))]

        r = [[[-1 for j in range(len(x))] for i in range(10)] for k in range(le)]

        print(r)
        for k in range(le):
            tem = [x[j] for j in range(len(x))]
            t = [t1[j] for j in range(len(t1))]

            for i in range(0, len(x), +1):

                a = (tem[i] % 10)
                j = 0
                while (r[k][a][j] != -1):
                    j = j + 1

                r[k][a][j]=i
                # r[k][a].append(i)
                #print(i)
                tem[i] = int(tem[i] / 10)
                #print("tem:", tem)
            cou=0
            t1 = [-1 for j in range(len(x))]
            for i in range(0, 10, +1):
                for j in range(0, len(x), +1):
                    if (r[k][i][j] != -1):
                        t1[cou] = t[r[k][i][j]]
                        x[cou] = tem[r[k][i][j]]
                        cou = cou + 1

        return t1


class sort:
    def __init__(self, ar):
      tem = []
      for i in range(3):
        x = fun1.make(self, ar, i+1)
        print(x)
        y= fun2.make(self,x,i+1)
        #print(y)

        #tem = [ar[j] for j in range(len(ar))]
        tem =tem+y
      print (tem)

ar = [12, 36, 44, 11, 5,22,17,89, 4, 9, 6, 1, 10,0,678,342,100,235,564,563,573]
x = sort(ar)


