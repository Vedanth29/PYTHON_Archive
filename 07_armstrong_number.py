#Vedanth M
n = int(input("enter the number: "))
sum = 0
temp = n
while(temp>0):
    digit = temp%10
    sum+=digit**len(str(n))
    temp = temp//10
if sum == n:
    print("Amstrong")
else:
    print("Not Armstrong")
