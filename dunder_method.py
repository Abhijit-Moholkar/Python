class Employee:
    def __new__(cls, week1):
        inst = object.__new__(cls)
        return inst

    def __init__(self, week1):
        self.week_1 = week1

    
    def __add__(self, other):
        result = [x + y for x, y in zip(self.week_1, other.week_1)]
        return Employee(result)

    def __str__(self):
        return str(self.week_1)

    def __mul__(self, other):
        result = [x * y for x, y in zip(self.week_1, other.week_1)]
        return Employee(result)



hours1 = Employee([2,4,8,6,7,3,8])
rate1 = Employee([120, 130, 80, 90, 100, 150, 180])
amount1 = hours1 * rate1
hours2 = Employee([4,2,8,6,9,7,5]) 
rate2 = Employee([200, 50, 250, 20, 800, 10, 1000])
amount2 = hours2 * rate2
total = amount1 + amount2
print(f"amount recieved by employee1 and Employee2 in week are\n {amount1}\n{amount2}")

print(f"Total hours of work in week1 are f{total}")
'''
Output
amount recieved by employee1 and Employee2 in week are
 [240, 520, 640, 540, 700, 450, 1440]
[800, 100, 2000, 120, 7200, 70, 5000]
Total hours of work in week1 are f[1040, 620, 2640, 660, 7900, 520, 6440]
'''
