t = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]
e = 0
s = 5
i = 0
count = 1

while (i < 3):

    for h in (range(e, s, +1)):
        t[e][h] = count
        count = count + 1

    for h in (range(e + 1, s, +1)):
        t[h][s - 1] = count
        count = count + 1

    for h in (range(s - 2, e - 1, -1)):
        t[s - 1][h] = count
        print("hai", h)
        count = count + 1

    for h in (range(s - 2, e, -1)):
        t[h][e] = count
        count = count + 1

    e = e + 1
    s = s - 1
    i = i + 1

for h in (range(0, 5, +1)):
    for i in (range(0, 5, +1)):
        print(t[h][i], end="  ")
    print("")
