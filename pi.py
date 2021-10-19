# To get math.pi number up to specified number of decimal points

from math import pi
n = int(input("Enter your number: "))
print(f'%.{n}f'%pi)
