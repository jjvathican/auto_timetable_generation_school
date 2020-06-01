p = 16


def make(f, p):
    for g in (range(1, f, +1)):
        print(end=" ")
    print(f, end="")
    for h in (range(f, p, +1)):
        print(end="  ")
    print(f)


for f in (range(1, p, +1)):
    make(f, p)
for f in (range(1, p, +1)):
    print(end=" ")
print(p)
for f in (range(p - 1, 0, -1)):
    make(f, p)

# second method of doing it
k = 1
a = +1;
p=p*2;
for m in (range(1, p)):
    for n in (range(1, p)):
        if (n == m and n == p - m):
            a = -1
        if (n == m or n == p - m):
            print(k, end="")
        else:
            print(end=" ")

    print("")
    k = k + a;
