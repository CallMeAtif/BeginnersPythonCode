class Employee:
    company = "Google"
    salary = 100000

Atif = Employee()
Parvez = Employee()
# a = Atif.salary
# b = Parvez.salary
# print(a,b)
a = Atif.salary = 200000
b = Parvez.salary = 300000
Atif.address = "Powai"
print(a)
print(b)
# below line throws an error because there is no address instance/class attribute for Parvez
# print(f"Parvez's address is: {Parvez.address}")
print(f"Atif's address is: {Atif.address}")