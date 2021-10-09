choice = 'y'
while(choice== 'y'.casefold()):
    first = input('Enter name of your attacking object from rock, paper, scissor: ')
    second = input('Enter name of your attacking object from rock, paper, scissor: ')
    if (first.casefold() == 'rock' and second.casefold() == 'scissor') or (first.casefold() == 'scissor' and second.casefold() == 'paper') or (first.casefold() == 'paper' and second.casefold() == 'rock'):
        print("Congradulations first you are a winner")
    else:
        print("Congradulations second you are a winner")
    choice = input("Do you want to start new game? if yes press y else no: ")
'''
Output

Enter name of your attacking object from rock, paper, scissor: rock
Enter name of your attacking object from rock, paper, scissor: scissor
Congradulations first you are a winner
Do you want to start new game? if yes press y else no: y
Enter name of your attacking object from rock, paper, scissor: paper
Enter name of your attacking object from rock, paper, scissor: scissor
Congradulations second you are a winner
Do you want to start new game? if yes press y else no: y
Enter name of your attacking object from rock, paper, scissor: paper
Enter name of your attacking object from rock, paper, scissor: rock
Congradulations first you are a winner
Do you want to start new game? if yes press y else no: n
'''
