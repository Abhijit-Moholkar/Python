# To reverse the list sequense through slicing

l = [10,20,30,40,50]
print(l[::-1])

###########################################

# To reverse the list sequence using append

l = [10,20,30,40,50]
l1 = []
for i in range(len(l),0,-1):
    print(l[i-1])
    
###########################################

# To reverse the list sequence using build in functions

l = [10,20,30,40,50]

print("reversed sequence of list elements is: ",list(reversed(l)))
