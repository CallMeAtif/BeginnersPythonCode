class Employee():
    company = "google"
    
    def showDetails(self):
        print(f"This is an Employee")

class Programmer(Employee):
    Language = "Python"

    def getLanguage(self):
        print(f"The Language is {self.Language}")
    
    def showDetails(self):
        print(f"This is a Programmer")   


a = Employee()
a.showDetails()
p = Programmer()
p.company
p.showDetails()
p.Language = "Golang"
p.getLanguage()
