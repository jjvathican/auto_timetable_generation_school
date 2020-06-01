def a_ar(ar,value):
    u = 0
    while (u < len(ar)):
        if (ar[u] == value):
            return 1
        u = u + 1
    if (u == len(ar)):
        return 0

# ar=[1,2,3,4,5,1,3,3]
# val=4
# out=a_ar(ar,val)
# print("out",out)#return 1 if value is found