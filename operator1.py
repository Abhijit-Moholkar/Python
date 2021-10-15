'''
print("Wellcome to python operators")
a = int(input("Please Enter First Number"))
b = int(input("Please Enter Second Number"))
c= int(input("Please Enter Third Number"))
while(True):
    choice=int(input("Enter 1 for Arithmatic Operations, 2 for Assignment Operations, 3 for Comparison operations, 4 for Logical Operations, 5 for Identity Operations, 6 Membership Operator, 7 Bitwise Operator"))
    if choice == 1:
        # Arithmatic Operators
        print("Wellcome to Arithmatic Operation")
        print("Addition of {} and {} is: ".format(a,b),a+b)
        print(f"Subtraction of {a} and {b} is: ",a-b)
        print("Multiplication of {} and {} is: ".format(a,b),a*b)
        print("Division of {} and {} is: ".format(a,b),a/b)
        print("Remainder of {} and {} is: ".format(a,b),a%b)
        print("Power of {} and {} is: ".format(a,b),a**b)
        print("Floor Division of {} and {} is: ".format(a,b),a//b)

    elif choice == 2:
        # Assignment Operators
        print("Wellcome to Assignment Operation")
        c = b
        print("value of new object c after = operation is",c)
        c += b
        print("value of object c after += operation is",c)
        c -= b
        print("value of object c after -= operation is",c)
        c *= b
        print("value of object c after *= operation is",c)
        c /= b
        print("value of object c after /= operation is",c)
        c **= b
        print("value of object c after **= operation is",c)
        c //= b
        print("value of object c after //= operation is",c)
        c %= b
        print("value of object c after %= operation is",c)
        c = int(c)
        c &= b
        print("value of object c after &= operation is",c)
        c |= b
        print("value of object c after |= operation is",c)
        c <<= b                           
        print("value of object c after <<= operation is",c)
        c >>= b
        print("value of object c after >>= operation is",c)
        c ^= b
        print("value of object c after ^= operation is",c)

    elif choice == 3:
        # Comparison Operators
        print("Wellcome to comparison operators")
        print("Value of a and b are",a,b)
        print("Result of {} == {} comparison operator is: ".format(a,b),a == b)
        print("Result of {} != {} comparison operator is: ".format(a,b),a != b)
        print("Result of {} < {} comparison operator is: ".format(a,b),a < b)
        print("Result of {} > {} comparison operator is: ".format(a,b),a > b)
        print("Result of {} <= {} comparison operator is: ".format(a,b),a <= b)
        print("Result of {} >= {} comparison operator is: ".format(a,b),a >= b)

    elif choice == 4:
        # Logical Operators
        print("Wellcome to Logical Operators")
        print("Result of a>b & b<c operation is: ",(a>b) & (b<c))
        print("Result of a>b | b<c operation is: ",(a>b) | (b<c))
        print("Result of !(a>b) operation is: ",not(a>b))
        
    elif choice == 5:
        # Identity operators
        print("Wellcome to Identity Operators")
        print("Result of a is a operation is: ",a is a)
        print("Result of a is not a operation is: ",a is not a)

    elif choice == 6:
        #Membership Operator
        print("Wellcome to Membership Operators")
        l=[1,2,3,4,5,6,7,8,9,10]
        print(f"{b} is member of {l} result as ",b in l)

    elif choice == 7:
        #Bitwise Operator
        print("Wellcome to Bitwise Operators")
        print(a,b)
        b=2
        print("Result of a & b operation is: ",a & b)
        print("Result of a|b operation is: ",a | b)
        print("Result of ~ a operation is: ",~ a)
        print("Result of a>>b operation is: ",a>>b)
        print("Result of a<<b operation is: ",a<<b)
        print("Result of a^b operation is: ",a^b)
     '''
import operator   

a = 10; b= 5
print(f"Addition of {a} and {b} is: {operator.add(a, b)}")
print(f"Subtraction of {a} and {b} is: {operator.sub(a, b)}")
print(f"Multiplication of {a} and {b} is: {operator.mul(a, b)}")
print(f"Division of {a} and {b} is: {operator.itruediv(a, b)}")
print(f"Floor division of {a} and {b} is: {operator.floordiv(a, b)}")
print(f"{a} power of {b} is: {operator.pow(a,b)}")
print(f"Floor division of {a} and {b} is: {operator.abs(a)}")
print(f"Result of {a} less than {b} is: {operator.lt(a,b)}")
print(f"Result of {a} greater than {b} is: {operator.gt(a,b)}")
print(f"Result of {a} less than or equal to is: {operator.le(a,b)}")
print(f"Result of {a} greater than {b} is: {operator.ge(a,b)}")
print(f"Result of {a} less than or equal to is: {operator.ne(a,b)}")
print(f"Result of {a} greater than {b} is: {operator.eq(a,b)}")
print(f"Result of {a} less than or equal to is: {operator.le(a,b)}")

a = 1
b = 0
print(operator.iand(a,b))
print(operator.ior(a,b))
print(operator.xor(a,b))
print(operator.invert(b))
