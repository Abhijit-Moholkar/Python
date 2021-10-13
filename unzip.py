# Accepting multiple inputs in single line using split function

x, y, z = input("Enetr Three values: ").split()
print("Value of x is {}, y is {} and value of z is {}".format(x,y,z))
print(f"Adiition of {int(x)} ,{int(y)}, and {int(z)} is {int(x) + int(y) + int(z)}")

'''
Output

Enetr Three values: 10 15 20
Value of x is 10, y is 15 and value of z is 20
Adiition of 10 ,15, and 20 is 45
'''
#######################################################
# Accepting multiple inputs in single line using List comprehenssion

x, y, z = [int(x) for x in input("Enter values of x, y, and z ").split()]
print(f"Value of x is {x}, y is {y}, and z is {z}")
print(x + y + z)

'''
Output

Enter values of x, y, and z 10 15 20
Value of x is 10, y is 15, and z is 20
45
'''
