#Vedanth M

for i in range(0,10):
    n = int(input("enter the num::"))
    if(n==2 or n==3 or n==5 or n==7):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
    if (n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0):
        print(f"{n} is a prime number")
    break
