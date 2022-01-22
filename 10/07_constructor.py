class Employee:
    company = "Google"
    def getsalary(self, signature):
        print(f"The salary of the Employee working in {self.company} is {self.salary}\n{signature}")

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")
        
    @staticmethod #in static method functions can be used without (self)
    def greet():
        print("Good Morning, Sir")
    
    @staticmethod
    def time():
        print("The time is 12PM in the Afternoon")

Parvez = Employee("Parvez", 100 ,"YouTube")
# Parvez = Employee()# --> this throws an error (missing 3 required positional arguments: 'name', 'salary', and 'subunit')
Parvez.getDetails()