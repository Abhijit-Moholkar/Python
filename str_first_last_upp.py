s = 'python'
s = s[0].upper() + s[2:-1] + s[-1].upper()
print(s)
'''
Output
pythoN
'''

s = 'python'
a = ''
for i in range(len(s)) :
    if i == 0 | i == (len(s) - 1):
        a += s[i].upper()
    else:
        a += s[i]
print(a)
'''
Output
pythoN
'''
