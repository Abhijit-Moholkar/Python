a = 10 
b = 5
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (b, a) [a < b] )  
#############################################

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# elif [a<b] is false then value of False key will print
print({True: a, False: b} [a < b])

###############################################

print((lambda: b, lambda: a)[a < b]())
###############################################
