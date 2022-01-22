class Person:
    country = "India"

    def __init__(self):
        print("Initializing person\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing employee\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self):
        super().__init__()
        print("Initializing programmer\n")

    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Progarmmer so I am breathing++..")

# p = Person()
# p.takeBreath()
# print(p.company) # throws an error

# e = Employee()
# e.takeBreath()
# print(e.company)

pr = Programmer()
# pr.takeBreath()
# print(pr.company)
# print(pr.country)
