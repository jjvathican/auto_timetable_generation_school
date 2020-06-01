

class calculate:
    def __init__(self):
        hehe=0
        # print("")
        # y=teach()

    def make(self, str):
        cal = 0
        cal1=0
        l=len(str)
        for i in range(l):
            # print(len(str))
            # if ((str[i] >= 'a' and str[i] <= 'f')):
            #     print(i)
            def f(x):
                return {
                    'A': 10,
                    'B': 11,
                    'C': 12,
                    'D': 13,
                    'E': 14,
                    'F': 15,

                }.get(x, x)

            # z=f(str[i])
            # print(z)



            z = f(str[l-i-1])
            cal = cal + int(z) * 16**i
            # cal1= cal1*10+int(z)
            # print(cal)
            # print(cal1)
        a=0
        mul=0
        while(cal>0):
            #print("jerin")
            #print("cal:",cal)
            r = cal % 2
            mul=mul+(10**a)*r
            #print("r:",r)
            cal=int(cal/2)
            a=a+1
        #mul.format(10)
        #mul= bin(ffff)
        #"{0:b}".format(10)
        # print("mul:",mul)
        return mul

# str = "0A"
# m = calculate()
# y = calculate.make(m, str)
# print(y)
