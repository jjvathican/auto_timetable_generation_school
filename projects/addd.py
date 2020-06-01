

def sumit(x):
  sum=[]
  hi=max(x)
  # print("hi",hi)
  c=0
  while(hi>0):
      hi=int(hi/10)
      c=c+1;
  # print("c",c)

  # print("hi",hi)
  for j in range(c):
      add=0
      for i in range(len(x)):
        m = x[i] % 10
        add=add+m
        x[i]=int(x[i]/10)
      sum=sum+[add]
  return sum









# x=[1001,0,110,1000000,1010101]
# y=sumit(x)
# print(y)