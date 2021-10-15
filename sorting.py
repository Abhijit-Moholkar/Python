
# Implementation of bubble sort
      
l = [5,2,8,6,7,1,3,4,6]
for i in range(1,len(l)):
    for j in range(1,len(l)-i+1):
        if l[j-1]>l[j]:
            l[j-1],l[j] = l[j],l[j-1]
        
print(l)
##############################################

# Implementation of selection sort
l = [5,2,8,6,7,1,3,4,6]
l2=[]
for i in range(len(l)):
    l2.append(min(l))
    l.remove(min(l))
print(l2)
###############################################

# Implementation of insertion sort
l = [5,2,8,6,7,1,3,4,6]
for i in range(1,len(l)):
    key =l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
    print(l)
