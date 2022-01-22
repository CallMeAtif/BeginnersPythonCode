class Employee():
    company = "Doxper"
    salary = 100
    location = "Mumbai"

    @classmethod
    def addsal(cls,sal):
        cls.salary = sal

parvez = Employee()
print(parvez.company)
# parvez.addsal(500)
parvez.salary = 200
print(parvez.salary)
print(Employee.salary)