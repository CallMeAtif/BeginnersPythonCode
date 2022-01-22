class Employee():
    company = "Realme"
    salary = 5000
    salarybonus = 500

    @property#property method is called getter method
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary


e = Employee()
e.totalsalary = 5600
print(e.salary)
print(e.salarybonus)
print(e.totalsalary)