cstr = "I love python"
   
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
#############I love python##############
The left aligned string is :
I love python---------------------------
The right aligned string is :
---------------------------I love python
'''
