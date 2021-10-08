while True:
    i = int(input("Please enter Number of units you have consumed: "))
    if i <= 100:
        charge = 0
    elif i <= 200:
        charge = (i - 100) * 5
    else:
        charge = ((i-200) * 8) + ((i-100) * 5)

    print(f"Your Electricity bill for {i} consumed units is {charge}")

'''
output
Please enter Number of units you have consumed: 100
Your Electricity bill for 100 consumed units is 0
Please enter Number of units you have consumed: 350
Your Electricity bill for 350 consumed units is 2450
Please enter Number of units you have consumed: 150
Your Electricity bill for 150 consumed units is 250
'''
