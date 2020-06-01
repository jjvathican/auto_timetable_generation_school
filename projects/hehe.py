from he2 import b_count


def seek(id,cal):
        count = [0 for i in range(len(id))]
        ar = []
        br=[]
        i = 0
        a = 1
        for rev in range(cal):
           for k in range((len(id)+1)*2):
                if (i >= len(id) or i < 0):
                   a = a * -1
                   br=br+[ar]
                   ar=[]
                else:
                   q,w=b_count(count[i], id[i], ar)
                   ar = ar + [q]
                   count[i]=w
                i = i + a
           br[len(br)-1].reverse()
        print(count)

        return br


# id = [[4, 5, 6], [1, 2, 3],[1,4]]
# a=seek(id,10)
# print("a",a)
# # try:
#     except:
#     ar[i] = 0
#     i = i + 1
# count[i]=-1
# try:
#  print("ei", i)
#  ar[i]=0
#  i=i+1
#  count[i] = -1
# except:
#     break
# ar[i] = 0
# i = i - 1
# print("i", i)
# print("count[i]", count[i])
# print("ar", ar)
# i=0
# if(x==2):
#     return x,i
# else:
#     p,e=fun(x+1)
#     while (id[x][i] == id[p][e] and i!=len(id[p])):
#         e=e+1
#     print(x,id[p][e])
#     return x,i


# i = 0
# print(x,id[x][i])
#
#     i=i+1
# else:
#     print("hai",x)
#     # ae=ae+[x]
#     return x




# def calc_factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x - 1))
#
#
# num = 4
# print("The factorial of", num, "is", calc_factorial(num))
