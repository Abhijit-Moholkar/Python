s = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]

print([[j for j in i.split() if j not in ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']]for i in s])

'''
Output

[['new', 'world', 'record', 'was', 'set'], ['holy', 'city', 'ayodhya'], ['eve', 'diwali', 'tuesday'],
 ['over', 'three', 'lakh', 'diya', 'or', 'earthen', 'lamps'], ['lit', 'up', 'simultaneously', 'banks', 'sarayu', 'river']]
'''
