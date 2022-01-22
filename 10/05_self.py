class Employee:
    company = "Google"
    def getsalary(self):
        print(f"The salary of the Employee working in {self.company} is {self.salary}")

Parvez = Employee()
Parvez.salary = 100000
Parvez.getsalary() #Employee.getsalary(Parvez)