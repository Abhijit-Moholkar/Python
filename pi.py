# To get math.pi number up to specified number of decimal points

from math import pi
n = int(input("Enter your number: "))
print(f'%.{n}f'%pi)


##############################################################

# To get math.pi number up to specified number of decimal points

from math import pi
i = int(input("Enter your number: "))

str(math.pi).split('.')[0]+'.'+str(math.pi).split('.')[1][:i]
