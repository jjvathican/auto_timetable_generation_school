def radixsort(aList,bList):
    RADIX = 10
    # bList = br#[x  for x in range(1,len(aList)+1)]
    #bList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(bList))
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]
        pos=[list() for _ in range (RADIX)]

        # split aList between lists
        a=0
        for i in aList:
            tmp = int (i / placement)
            #tmp1=int(aList[a]/placement)
            buckets[tmp % RADIX].append(i)
            pos[tmp % RADIX].append(bList[a])
            a+=1


            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        a = 0
        #print(pos)
        for b in range(RADIX):
            buck = pos[b]
            for i in buck:
                bList[a] = i
                #print(i)
                a+=1

        # move to next digit
        placement *= RADIX
        # print(placement)

    return(aList,bList)
# ar = [0,68,1,0,7]
# br=[1,2,3,4,5]
# a,b=radixsort(ar,br)
# print("a",a)
# print("b",b)
# a.reverse()
# b.reverse()
# print(a,b)