# problem statement: Take int input i,j,k,n from user..make all combinations of i,j,k ..
# print only those combinations whose sum is not equal to n.

i = int(input("Enter first number: "))
j = int(input("Enter second number: "))
k = int(input("Enter third number: "))
n = int(input("Enter fourth number")) 
maxima = max(i,j,k)
l = [(a,b,c) for a in range(i+1) for b in range(j+1) for c in range(k+1) if (a in [0,i]) and (b in [0,j]) and (c in [0,k]) and (a+b+c) != n]
print(l)

output
Enter first number: 4
Enter second number: 5
Enter third number: 6
Enter fourth number10
[(0, 0, 0), (0, 0, 6), (0, 5, 0), (0, 5, 6), (4, 0, 0), (4, 5, 0), (4, 5, 6)]
