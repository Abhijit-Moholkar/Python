class c2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"2d vector is {self.icap}i + {self.jcap}j"
    
class c3dvec(c2dvec):
    def __init__(self,i,j,k):
        #self.icap=i
        #self.jcap=j
        super().__init__(i,j)
        self.kcap=k
       
    def __str__(self):
        return f"3d vector is {self.icap}i + {self.jcap}j + {self.kcap}k"

c2d=c2dvec(2,3)
print(c2d)
c3d=c3dvec(4,5,6)
print(c3d)

'''
Output
2d vector is 2i + 3j
3d vector is 4i + 5j + 6k
'''
