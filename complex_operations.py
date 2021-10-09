a = int(input("Enter real part of first complex number"))
b = int(input("Enter imaginary part of first complex number"))
s = complex(a,b)
print(f"First complex number is: {s}")
l = s.real
m = s.imag

p = int(input("Enter real part of second complex number"))
q = int(input("Enter imaginary part of second complex number"))
g = complex(p,q)
print(f"Second complex number is: {g}")
e = g.real
f = g.imag

choice = 'y'
while(choice.casefold() == 'y'):
    h=int(input("Enter which operation to be performed on complex Numbers a for addition, 2 for subtrction, 3 for multiplication, and 4 for division"))
    if h==1:
        c = l + e
        d = m + f
        r = complex(c,d)
        print(f"Addition of complex numbers {s} ad {g} is {r}")

    elif h==2:
        c = l - e
        d = m - f
        r = complex(c,d)
        print(f"Subtraction of complex numbers {s} ad {g} is {r}")

    elif h==3:
        c = (l * e) - (m * f)
        d = (l * f) + (e * m)
        r = complex(c,d)
        print(f"Multiplication of complex numbers {s} ad {g} is {r}")
    
    elif h==4:
        c = ((l * e) + (m * f)) / (e*e-f*f)
        d = ((e * m) - (l * f)) / (e*e-f*f)
        r = complex(c,d)
        print(f"Division of complex numbers {s} ad {g} is {r}")
    choice = input("Do you want to continue? Enter y if yes else n: ")

'''
Output
Enter real part of first complex number5
Enter imaginary part of first complex number6
First complex number is: (5+6j)
Enter real part of second complex number2
Enter imaginary part of second complex number3
Second complex number is: (2+3j)
Enter which operation to be performed on complex Numbers a for addition, 2 for subtrction, 3 for multiplication, and 4 for division1
Addition of complex numbers (5+6j) ad (2+3j) is (7+9j)
Do you want to continue? Enter y if yes else n: y
Enter which operation to be performed on complex Numbers a for addition, 2 for subtrction, 3 for multiplication, and 4 for division2 
Subtraction of complex numbers (5+6j) ad (2+3j) is (3+3j)
Do you want to continue? Enter y if yes else n: y
Enter which operation to be performed on complex Numbers a for addition, 2 for subtrction, 3 for multiplication, and 4 for division3
Multiplication of complex numbers (5+6j) ad (2+3j) is (-8+27j)
Do you want to continue? Enter y if yes else n: y
Enter which operation to be performed on complex Numbers a for addition, 2 for subtrction, 3 for multiplication, and 4 for division4
Division of complex numbers (5+6j) ad (2+3j) is (-5.6+0.6j)
Do you want to continue? Enter y if yes else n: n
'''  
