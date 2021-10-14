# Code to perform addition of numbers upto input number using for loop

n = int(input("Enter your number: "))
sim=0
for i in range(1,n+1):
    sim+=i
print(f"Addition result is {sim}")

# Output
# Enter your number: 7
# Addition result is 28

#############################################################

# Code to perform addition of numbers upto input number using while loop

sim = 0
n = int(input("Enter your number: "))
i=1
while(i<n+1):
    sim+=i
    i+=1
print(f"Addition result is {sim}")

# Output
# Enter your number: 7
# Addition result is 28

#############################################################

# Code to perform addition of numbers upto input number using recurssion method

n = int(input("Enter your number: "))
def add(n,sim):
    
    if n>0:
        sim+=n
        add(n-1,sim)
    else:
        print(f"Addition result is {sim}")

add(n,sim=0)

# Output
# Enter your number: 7
# Addition result is 28

#############################################################
'''
# Code to perform addition of numbers upto input number using heigher order function

from functools import reduce

n = int(input("Enter your number: "))
l = range(1, n+1)
result = reduce(lambda x,y : x+y, l)
print(f"Addition result is {result}" )

# Output
# Enter your number: 7
# Addition result is 28
