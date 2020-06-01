t = [[7, 16, 9, 10],
     [5, 15, 11, 13],
     [1, 2, 3, 7],
     [4, 12, 7, 8]]
temp=0
for g in (range(0, 4, +1)):
    for h in (range(0, 4, +1)):
        if (temp < t[g][h]):
            temp = t[g][h]
            p = h
    for h in (range(0, 4, +1)):
        if (temp > t[h][p]):
            temp = t[h][p]
            p1 = h
    if (t[g][p]==t[p1][p]):
        print(t[g][p])
    #(t[g][p])