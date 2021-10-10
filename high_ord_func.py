l = [4, 5, 3, 9, 8, 9, 2, 6, 10]

def squar(n):
    return n**2

def gt_th_50(m):
    if m>50:
        return m

m = list(map(squar , l))
print(f"Squar of given numbers is {m}")

o = list(filter(gt_th_50 , m))
print(f"{o} squar are greater than 50")

from functools import reduce

p=reduce(lambda a,b:a+b , o)
print(f"sum of numbers is {p}")

'''
Output
Squar of given numbers is [16, 25, 9, 81, 64, 81, 4, 36, 100]
[81, 64, 81, 100] squar are greater than 50
sum of numbers is 326
'''
