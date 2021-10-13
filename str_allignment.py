cstr = "I love geeksforgeeks"
   
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))

'''
output
Center aligned string with fillchr:
##########I love geeksforgeeks##########
The left aligned string is :
I love geeksforgeeks--------------------
The right aligned string is :
--------------------I love geeksforgeeks
'''
