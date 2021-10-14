# Code to check string for anagram

s = 'anagram'
s1 = input("Enter your string: ")

for i in s1:
    if i in s:
        pass
    else:
        print('String is not anagram')
        break
else:
    print('String is anagram')

# Output
# Enter your string: anam
# String is anagram
# Enter your string: amgh
# String is not anagram
