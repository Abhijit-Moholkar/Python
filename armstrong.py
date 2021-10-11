l1=[]
for i in range(1,1001):
    s=str(i)
#print(len(s))
    su=0
    for j in range(len(s)):
        su+=int(s[j])**len(s)
    if su == i:
       l1.append(i) 
print(l1)

Output

[1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
