#Factorial finding using reduce function
from functools import reduce
n = int(input("Enter number whose factorial you want to find: "))
l = []
for i in range(n,0,-1):
    l.append(i)
print(l)
print(f"Factorial of {n} = {reduce(lambda x,y:x*y,l)}")
##############################################################  
# Factorial using iter
a = int(input("Enetr Number whose factorial you want to find: ")) 
j=0
h = []
while a>0:
    h.insert(j,a)
    a=a-1
    j=j+1

print(h)
ier=iter(h)
    
fact = 1
for k in range(len(h)):
    fact=fact*ier.__next__()
print(fact)
##############################################
# Factorial using for loop
a = int(input("Enter number for which you want to find factorial: "))
b = a
fact = 1
for i in range(1, a+1):
    if a == 0 or a == 1:
        break
    else:
        fact = fact * i

print(f"factorial of {b} is {fact}")
########################################################
# To calculate Factorial of a number using while loop
a=int(input("Enter number for which you want to find factorial: "))
b=a
fact=1
while a!=1:
    if a==0:
        break
    else:
        fact=fact*a
        a=a-1

print(f"factorial of {b} is {fact}")
