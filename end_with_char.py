s = "hello good morn2in3g all. I we4llcome a7ll in pythh2on couurse"
flag = False
if s.endswith('ll'):
    print("entire string ends with ll")
    flag == True
else:
    l = s.split()
    
    for i in l:
        if i.endswith('ll'):
            print(f"word at position {l.index(i)+1} ends with ll")
            flag = True
        else:
            continue
    if  flag == False:
        print("No any word ends with ll")

'''
output
word at position 7 ends with ll
'''
