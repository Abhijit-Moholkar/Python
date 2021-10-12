# Code to count character occurrences  in string

s1 = 'python is intresting language'
d = {}
for i in s1:
    d.update({i:s1.count(i)})
print(d)

# Output
# {'p': 1, 'y': 1, 't': 3, 'h': 1, 'o': 1, 'n': 4, ' ': 3, 'i': 3, 's': 2, 'r': 1, 'e': 2, 'g': 3, 'l': 1, 'a': 2, 'u': 1}
#############################################################

# Code to count character occurrences  in string

s1 = 'python is intresting language'
d = {}
for i in s1:
    d[i] = s1.count(i)
print(d)

# Output
# {'p': 1, 'y': 1, 't': 3, 'h': 1, 'o': 1, 'n': 4, ' ': 3, 'i': 3, 's': 2, 'r': 1, 'e': 2, 'g': 3, 'l': 1, 'a': 2, 'u': 1}
#############################################################

# Code to count character occurrences  in string

s1 = 'python is intresting language'
l = []
for i in s1:
    l.append((i,s1.count(i)))
print(set(l))

# Output
{('y', 1), ('h', 1), ('p', 1), ('i', 3), ('g', 3), ('e', 2), ('t', 3), (' ', 3), ('u', 1), ('r', 1), ('l', 1), ('o', 1), ('n', 4), ('s', 2), ('a', 2)}
