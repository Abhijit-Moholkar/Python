# To remove duplicates of list using remove method
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

# To remove duplicates of list using another list

l=[2,4,5,3,6,8,2,4,3,1,5,6,6,6,6]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
'''
Output
[2, 4, 5, 3, 6, 8, 1]
'''

# To remove duplicates of list using set property

l=[2,4,5,3,6,8,2,4,3,1,5,6,6,6,6]
print(list(set(l)))

'''
Output
[2, 4, 5, 3, 6, 8, 1]
'''
