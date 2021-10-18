from random import random
n = random()*100+100
n = int(n)
print(n)

a = (n//100)%10
b = (n//10)%10
c = n%10
print(a + b + c)
