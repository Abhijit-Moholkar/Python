# Code to add elements excluding in between 6 and 7

l = [1, 6, 2, 2, 7, 1, 6, 99, 99, 7]
sim = 0
i =0
while i<len(l):
    if l[i] == 6:
        while l[i]!=7:
            i+=1
            continue
        i+=1
    else:
        sim += l[i]
        i+=1
print(sim)    

# Output
# 2
