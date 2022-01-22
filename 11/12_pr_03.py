class Employee:
    salary = 14500
    increment = 500    
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment
        
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,val):
        self.increment = val - self.salary

e = Employee()
# print(p.salaryAfterIncrement(20000))
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 20000
print(e.salaryAfterIncrement)
print(e.increment)