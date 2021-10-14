# Anagram 
s = 'anagram'
if s == s[::-1]:
    print("Congratulations!!! String is anagram string")
else:
    print("Sorry!!! String is not anagram string")

##############################################################

s = "Wellcome to pyhon. It is very intresting language. Wellcome to pyhon. Wellcome to pyhon."


s = 'anagram'

if s == s[::-1]:
    print("Congratulations!!! String is anagram string")
else:
    print("Sorry!!! String is not anagram string")
##############################################################

s = 'anagram'
if s == reversed(s):
    print("Congratulations!!! String is anagram string")
else:
    print("Sorry!!! String is not anagram string")
##############################################################

s = 'anagram'
l = len(s)
s1= ''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
if s1 == s:
    print("Congratulations!!! String is anagram string")
else:
    print("Sorry!!! String is not anagram string")
    
