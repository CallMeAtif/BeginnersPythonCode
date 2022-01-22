class Employee:
    company = "Google"
    def getsalary(self, signature):
        print(f"The salary of the Employee working in {self.company} is {self.salary}\n{signature}")
        
    @staticmethod #in static method functions can be used without (self)
    def greet():
        print("Good Morning, Sir")
    
    @staticmethod
    def time():
        print("The time is 12PM in the Afternoon")

Parvez = Employee()
Parvez.salary = 100000
Parvez.getsalary("Thanks")
Parvez.greet()
Parvez.time()
# Parvez.getsalary() #Employee.getsalary(Parvez)