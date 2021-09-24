#Vedanth M
n = int(input("enter the range to check prime numbers::"))
for i in range(2,n):
     if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
         print(i)
     if(i==2 or i==3 or i==5 or i==7):
         print(i)
