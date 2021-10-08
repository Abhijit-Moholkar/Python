#Finding names of male employees from dict
dict = {'Amol' : 'M', 'Shruti' : 'F', 'Suresh' : 'M', 'Madhuri' : 'F'}
print(list(filter(lambda x:dict[x]=='M',dict)))
