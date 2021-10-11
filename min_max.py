l=[17,34,-55,67,-93,12,34,567,89]

l1=[]
l2=[]
l3=[]
l4=[]
for i in l:
    if i>0:
        if i%2==0:
            l1.append(i)
        else:
            l3.append(i)
    else:
        if i%2==0:
            l2.append(i)
        else:
            l4.append(i)
print("List l1 is ",l1)
print("List l2 is ",l2)
print("List l3 is ",l3)
print("List l4 is ",l4)
print("Minimum number out of positive even numbers is: ",min(l1))
print("Maximum number out of positive even numbers is: ",max(l1))
print("Minimum number out of positive odd numbers is: ",min(l3))
print("Maximum number out of positive odd numbers is: ",max(l3))

# print("Minimum number out of negative even numbers is: ",min(l2))
# print("Maximum number out of negative even numbers is: ",max(l2))
print("Minimum number out of negative odd numbers is: ",min(l4))
print("Maximum number out of negative odd numbers is: ",max(l4))

'''
Output
List l1 is  [34, 12, 34]
List l2 is  []
List l3 is  [17, 67, 567, 89]
List l4 is  [-55, -93]
Minimum number out of positive even numbers is:  12
Maximum number out of positive even numbers is:  34
Minimum number out of positive odd numbers is:  17
Maximum number out of positive odd numbers is:  567
Minimum number out of negative odd numbers is:  -93
Maximum number out of negative odd numbers is:  -55
'''
