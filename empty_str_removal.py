# Remove empty string from list using for loop

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
l = []
for i in list1:
    if i != '':
        l.append(i)
print(l)
##############################################################

# Remove empty string from list using for loop

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#[list1.remove(i) for i in list1 if i == ' ' ]
for i in list1:
    if i == '':
        list1.remove(i)
print(list1)
##############################################################


