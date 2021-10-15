n = int(input("Enter your number"))
l =[n]
while(n!=1):
    if n%2 == 0:
        n /= 2
        l.append(n)
    else: 
       n = n*3+1
       l.append(n)
print(l)
