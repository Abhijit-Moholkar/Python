
s={(1,2,3),4,5}
print(s)
print(type(s))
s=s.union({6,7,8})
print("union is ",s)
m={(4,5,6,(1,2,3))}
n=s.intersection({(1,2,3),7,8})
print("intersection is: ",n)
print(n.isdisjoint(s))
print(n.issubset(s))
print(s.issuperset(n))
l=m.difference(s)
print(l)
p=m-s
print(p)
p.clear()
print(p)
q=5 in s
print(q)


s = {1,2,3}
s2 = {1,2}
s.add(4)
print(s)
s1 = s.copy()
print(s1)
s3 = s.difference(s2)

print(s3)
print(s3.pop())
s1 = {1,2,3,4}
print(s1.discard(3))
print(s1)
s1.difference_update(s2)
print(s1)
s = {1,2,3,4,5,6,7}
s1 = {1,2}
print(s)
print(s.intersection(s1))
a = s & s1
print(a)
print(s.isdisjoint(s1))
print(s1.issubset(s))
print(s.issuperset(s1))
print('a',s.symmetric_difference(s1))
s.symmetric_difference_update(s1)
print(s)
print(s.union(s1))
s.clear()
print(s)
s = {()}
s1= set()
s2 = set([])
s3 = frozenset()
print(type(s),type(s1),type(s2), type(s3))




