l=[2,4,5,3,6,8,2,4,3,1,5,6,6,6,6]
for i in l:
    c= l.count(i)
    if c>1:
        for j in range(c-1):
            l.remove(i)
print(l)

'''
Output
[3, 8, 2, 4, 3, 1, 5, 6]
'''
