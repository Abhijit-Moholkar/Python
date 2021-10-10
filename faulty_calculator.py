print("Wellcome to project!!! you have 10 repitations")
i=1
while i in range(10):
    operator=input("enter which operation you want to perform either +,*, or /: ")
    operand1=int(input("Enter First Operand: "))
    operand2=int(input("Enter second operand: "))

    if operator=="+":
        if operand1==56 and operand2==9:
            print(f"Result is 77")
        else:
            result=operand1+operand2
            print(f"Result of operation is {result}")


    elif operator=="*":
        if operand1==45 and operand2==3:
            print(f"Result is 555")
        else:
            result=operand1*operand2
            print(f"Result of operation is {result}")


    elif operator=="/":
        if operand1==56 and operand2==6:
            print(f"Result is 4")
        else:
            result=operand1/operand2
            print(f"Result of operation is {result}")

    else:
        print("you can try for only +,*,/ operations")
    
    i=i+1

'''
Output
Wellcome to project!!! you have 10 repitations
enter which operation you want to perform either +,*, or /: +
Enter First Operand: 56
Enter second operand: 9
Result is 77
enter which operation you want to perform either +,*, or /: +
Enter First Operand: 20
Enter second operand: 5
Result of operation is 25
enter which operation you want to perform either +,*, or /: *
Enter First Operand: 45
Enter second operand: 3
Result is 555
enter which operation you want to perform either +,*, or /: *
Enter First Operand: 8
Enter second operand: 4
Result of operation is 32
enter which operation you want to perform either +,*, or /: /
Enter First Operand: 56
Enter second operand: 6
Result is 4
enter which operation you want to perform either +,*, or /: /
Enter First Operand: 8
Enter second operand: 2
Result of operation is 4.0
enter which operation you want to perform either +,*, or /: -
Enter First Operand: 8
Enter second operand: 9
you can try for only +,*,/ operations
enter which operation you want to perform either +,*, or /:
'''
