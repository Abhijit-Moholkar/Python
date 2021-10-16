s ='sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
l = s.split()
print(list(filter(lambda x : x.isdigit() and int(x)>len(l),l)))
