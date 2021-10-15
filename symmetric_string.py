s = input("Enter your string: ")
l = int(len(s)/2)
if s[:l] == s[l:]:
    print("string is Symmetric")
else:
    print("String is not Symmetric")
    
#####################################################################
s = input("Enter your string: ")
l = int(len(s)/2)
for i in range(l):
    if s[i] == s[l+i]:
        pass
    else:
        print("String is not Symmetric")
        break
else:
    print("string is Symmetric")
####################################################################
s='sanjsan'
p=int(len(s)/2)
#print(p)
if s[0:p]==s[p:]:
    print('symmetric')
else:
    print('unsymmetric')
