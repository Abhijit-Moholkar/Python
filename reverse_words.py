# Code to reverse the words of string
s='Abhijit Vitthal Moholkar'
l1=[]
n=s.split()
s1 = ''
j = -1
for i in range(len(n)):
    s1 += n[j] + ' '
    j -= 1
    
print(s1)
'''
Output
Moholkar Vitthal Abhijit 
'''
#################################################

# Code to reverse the characters of words of string

s='Abhijit Vitthal Moholkar'
l1=[]
print(s[::-1])
n=s.split()
for i in n:
    l1.append(i[::-1])
print(' '.join(l1))
'''
Output
tijihbA lahttiV raklohoM
'''
##################################################

# Code to reverse the words along with characters of string

s='Abhijit Vitthal Moholkar'
l1=[]
n=s.split()
s1 = ''
j = -1
for i in range(len(n)):
    s1 += n[j][::-1] + ' '
    j -= 1
print(s1)
'''
Output
raklohoM lahttiV tijihbA
'''
##################################################

# Code to reverse the words and characters of string

s='Abhijit Vitthal Moholkar'
l1=[]
print(s[::-1])

# Output
# raklohoM lahttiV tijihbA
##################################################

# Code to reverse the characters of words of string

s='Abhijit Vitthal Moholkar'
l1=[]
#print(s[::-1])
n=s.split()
s1 = ''
for i in n:
    s1 += i[::-1] + ' '
print(s1)
'''
Output
tijihbA lahttiV raklohoM
'''
