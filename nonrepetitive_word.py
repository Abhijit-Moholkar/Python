s = "Wellcome to pyhon. It is very intresting language. Wellcome to pyhon. Wellcome to pyhon."
l = s.split()
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

s1 = ''+' '.join(l1)
print(s1)

# Output
# Wellcome to pyhon. It is very intresting language.
