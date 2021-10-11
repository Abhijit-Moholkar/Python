n1 = int(input("Enter first number: ")) 
n2 = int(input("Enter second number: "))
l1=[]
l2= []

for i in range(1,11):
    l1.append(n1*i)
    l2.append(n2*i)
print(l1)
print(l2)
for j in l1:
    if j in l2:
        print(f"least comman multiplier of {n1} and {n2} is: {j}")
        break

'''
Output
Enter first number: 2
Enter second number: 5
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
least comman multiplier of 2 and 5 is: 10
'''
