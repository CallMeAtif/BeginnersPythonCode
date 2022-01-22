class Employee():
    company = "Visa"
    eCode = 120

class Freelancer():
    company = "Fiverr"
    level = 0
    def updatelvl(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):
    programmer = "Parvez"

Parvez = Programmer()
Parvez.company
Parvez.updatelvl()
print(Parvez.level)