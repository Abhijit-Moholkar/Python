class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print(f"addition of {self.num} and {num2.num} is {self.num+num2.num}")
    
    def __sub__(self,num2):
        print(f"Subtraction of {self.num} and {num2.num} is {self.num-num2.num}")

    def __mul__(self,num2):
        print(f"Multiplication of {self.num} and {num2.num} is {self.num*num2.num}")

    def __truediv__(self,num2):
        print(f"Division of {self.num} and {num2.num} is {self.num/num2.num}")

    def __floordiv__(self,num2):
        print(f"Floor Division of {self.num} and {num2.num} is {self.num//num2.num}")


n1=Number(6)
n2=Number(2)

sum=n1+n2

sub=n1-n2

mul=n1*n2

truediv=n1/n2

floordiv=n1//n2
