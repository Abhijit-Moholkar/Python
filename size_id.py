a=10
b=10
c=10
print(id(a))
print(id(b))
print(id(c))

d=10.0
e=10.0
f=10.0000000001
j=10.0000000003
print(d.__sizeof__())
print(e.__sizeof__())
print(f.__sizeof__())
print(j.__sizeof__())
print(id(d))
print(id(e))
print(id(f))
print(id(j))

g='c'
h='c'
i='c'
print(id(g))
print(id(h))
print(id(i))
