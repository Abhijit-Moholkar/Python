# To find maximum length word and its possition

s1 = "Wellcome to pyhon. It is very intresting language. Wellcome to pyhon. Wellcome to pyhon."

l = {}
for i in s1.split():
    l.update({i:len(i)})
print(l)
for j in l:
    if l[j] == max(l.values()):
        print(j,l[j])

# Output
# {'Wellcome': 8, 'to': 2, 'pyhon.': 6, 'It': 2, 'is': 2, 'very': 4, 'intresting': 10, 'language.': 9}
# intresting 10
##################################################

# To find maximum length word and its possition

s = "Wellcome to pyhon. It is very intresting language. Wellcome to pyhon. Wellcome to pyhon."
l = s.split()
l1 = []
for i in l:
    l1.append((i,len(i)))
max=0
var = ''
for i in range(len(l1)):
    if max < l1[i][1]:
        max = l1[i][1]
        var = l1[i][0]

print(f"Maximum lenngth word is {var} and its length is {max}")

# Output
# Maximum lenngth word is intresting and its length is 10
