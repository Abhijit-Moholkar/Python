# Concatenate words of two strings using for loop

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i+j)
list3

###########################################################

# Concatenate words of two strings using list comprehenssion

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [x + y for x in list1 for y in list2]
list3
