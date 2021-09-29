#Vedanth M
import math
n = int(input("enter the number"))
x=0
y=0
flag = 0
if(n>0):
    x = (5*n*n + 4)
    s = int(math.sqrt(x))
    s = s*s
    if(x ==s):
        flag = 1
if(n>1):
    y = (5*n*n - 4)
    q = int(math.sqrt(x))
    if(y == q*q):
        flag = 1
if(flag == 1):
    print("fibonacci number")
else:
    print("not fibonacci")
