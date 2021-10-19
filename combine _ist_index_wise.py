# Code to cancatenate two lists index wise using zip function
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i,j in zip(list1,list2)]
   
list3

##########################################################

# Code to cancatenate two lists index wise using append method

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []

for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
list3
