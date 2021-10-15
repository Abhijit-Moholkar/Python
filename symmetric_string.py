s = input("Enter your string: ")
l = int(len(s)/2)
if s[:l] == s[l:]:
    print("string is Symmetric")
else:
    print("String is not Symmetric")
