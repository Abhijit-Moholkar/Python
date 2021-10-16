names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
l = list(filter(lambda a:a.istitle(),names))
print(len(''.join(l)))
