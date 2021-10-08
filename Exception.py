try:
    print(a)
except Exception as e:
    print(f"{e} Exception handled")
    try:
        if c == "harry":
            raise ValueError("harry is blocked")
    except Exception as e1:
        print(f"{e1} Exception handled")
        print("Wellcome to code Execution")
else:
    print("Code Executes successfully without exception")
finally:
    print("Thank you for executing this code")

'''
Output
Enter Your name: harry
name 'a' is not defined Exception handled
harry is blocked Exception handled
Wellcome to code Execution
Thank you for executing this code
'''
