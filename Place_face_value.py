i = int(input("Please Enter your number: ")) 
j = 1
while(i>0):
    
    if j == 1:
        print(f"Place value of {i%10} in your number is {1}")
        j = j *10
    else:
        print(f"Place value of {i%10} in your number is {j}")
        j = j *10
    i = i//10

'''
Ountput
Please Enter your number: 650
Place value of 0 in your number is 1
Place value of 5 in your number is 10
Place value of 6 in your number is 100
'''
