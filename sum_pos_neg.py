# Addition of positive and negative numbers using higher order functions

from functools import reduce

l = [2, 4, -6, -9, 11, -12, 14, -5, 17]

l1=list(filter(lambda x : x>0,l))
l2 = list(filter(lambda x : x<0,l))
print(f'Addition of positive elements is {reduce(lambda x,y : x+y,l1)}')
print(f'Addition of negative elements is {reduce(lambda x,y : x+y,l2)}')

##########################################################################

# Addition of positive and negative numbers using higher ordr functions

l = [2, 4, -6, -9, 11, -12, 14, -5, 17]

l1=list(filter(lambda x : x>0,l))
l2 = list(filter(lambda x : x<0,l))
print(f'Addition of positive elements is {sum(l1)}')
print(f'Addition of negative elements is {sum(l2)}')
