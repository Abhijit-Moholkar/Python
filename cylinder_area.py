from math import pi

r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

circle_area = 2 * (pi * r**2)

side_area = 2 * pi * r * h

area = circle_area + side_area

print("Area of cylinder is %.2f" %area)
