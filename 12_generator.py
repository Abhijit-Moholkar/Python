def gen(n):
    for i in range(n):
        yield i


h=[2,3,4,5,6,7,8,9]
ier=iter(h)

print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

'''
Output
2
3
4
5
6
7
8
'''
