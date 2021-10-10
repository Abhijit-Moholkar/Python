class Employee:
    company="Google"
    salary=120000
    print(company)
    
    def __init__(self):
        print(f"This is an employee of {self.company} and his salary is {self.salary}")
    
class Engineer(Employee):
    qualification="Engineer"
    def detail(self):
        print(f"This is an employee of {self.company} and his qualificatio is {self.qualification}")

class developer(Engineer, Employee):
    post="engineer"
    def rol(self):
        print(f"This is an employee of {self.company}, his qualification is {self.qualification} and his post is {self.post}")

class programmer(Employee):
    lang="py"
    company="youtube"
    
    def __init__(self):
        super().__init__()
        print(f"This is an employee of {self.company},he is working on language {self.lang} and his salary is {self.salary}")


emp=Employee() 
engg=Engineer()
engg.detail() 
dev=developer()
dev.rol() 
prog=programmer()

# Output 
# Google
# This is an employee of Google and his salary is 120000
#This is an employee of Google and his salary is 120000
#This is an employee of Google and his qualificatio is Engineer
#This is an employee of Google and his salary is 120000
#This is an employee of Google, his qualification is Engineer and his post is engineer    
#This is an employee of youtube and his salary is 120000
#This is an employee of youtube,he is working on language py and his salary is 120000
