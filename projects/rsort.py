import array


class sort:
    def __init__(self, ar):
        count=0
        while(n<):
            r = [[-1 for j in range(2)] for i in range(10)]
            le = 1
            for i in range(0, len(ar), +1):
                le = le * 10
                if (ar[i] < le):
                    count=count+1
                    val = ar[i]

                    for h in range(n):
                        val = int(val / 10)

                    # print(" fff",n)
                    a = (val % 10)
                    j = 0
                    while (r[a][j] != -1):
                        j = j + 1
                    print("j:", j)
                    r[a][j] = i  # int(ar[i] / 10)
                    cou = 0

            tem = [0 for i in range(0, 4, +1)]
            print("temp", tem)
            print(r)
            for i in range(0, 10, +1):
                for j in range(0, 2, +1):
                    if (r[i][j] != -1):
                        tem[cou]=ar[r[i][j]]
                       #ar[cou] = tem[]
                        cou = cou + 1

            print(ar)


ar = [12, 36, 44, 11]
x = sort(ar)
