l1 = [16,8,4,2] 
l2 = [16,8,2,4]

ratio = l1[1] / l1[0]
ratio2 = l2[1] / l2[0]
def prog(l,ratio):
    for i in range(1,len(l)):
        if l[i] / l[i-1] == ratio:
            continue
        else:
            print("List is not in Geometric progression")
            break
    else:
        print("List is in Geometric progression")

prog(l1,ratio)
prog(l2,ratio2)
