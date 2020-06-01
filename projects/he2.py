from he1 import a_ar
from random import randint
def b_count(count,id_p,ar):
    n=0
    while (n<len(id_p)*2):
        se= randint(0,len(id_p)-1)
        n=n+1
        count = count + 1
        if (a_ar(ar,id_p[se]) == 0):
            return id_p[se],count

    else:
        return 0,count
# count=0
# ar=[1,2,3,4]
# id=[[1,2,3,4],[3,2,4,2],[5,6,7,4]]
# out=b_count(count,id[0],ar)
# print("out",out)