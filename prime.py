n = 1
l = []
while (n<10000):
    for i in range(2,n):
        if n%i == 0:
            break
        else:
            continue
    else:
        l.append(n)
    n += 1
print(l[1000])
