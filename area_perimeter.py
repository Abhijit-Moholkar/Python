from math import sqrt
AB = float(input("Enter first side of right anle triangle: "))
AC = float(input("Enter second side of right anle triangle: "))
    
BC = sqrt(AB**2 + AC**2)

A = AB * AC / 2
p = AB + BC + AC

print("Area of right angled triangle is %.2f" %A)
print("Perimeter of right angled triangle is %.2f" %p)
