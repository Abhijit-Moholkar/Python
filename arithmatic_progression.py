l1 = [5,7,9,11,13,15] 
l2 = [2,5,7,8,12,14,16]

diff = l1[1] - l1[0]
diff2 = l2[1] - l2[0]
def prog(l,diff):
    for i in range(1,len(l)):
        if l[i] - l[i-1] == diff:
            continue
        else:
            print("List is not in arithmatic progression")
            break
    else:
        print("List is in arithmatic progression")

prog(l1,diff)
prog(l2,diff2)
