#Vedanth M
p = int(input("enter the Principle amount::"))
t = int(input("enter the Time::"))
r = int(input("enter the Ratio::"))

a = p * (pow((1+r/100),t))
ci = a - p
print(ci)
