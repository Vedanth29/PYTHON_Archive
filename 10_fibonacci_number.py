#Vedanth M

n = int(input("enter the size"))
f = 1
l = 1
print(f)
print(l)
for i in range(0,n-2):
    num = f + l
    f = l
    l = num
    print(num)
