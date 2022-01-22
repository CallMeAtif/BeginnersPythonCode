class Programmers:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name 
        self.product = product
    def getInfo(self):
        print("The name of the programmer is",self.name)
        print("The product he is working on is",self.product)

Atif = Programmers("Atif", "VS Code")
Parvez = Programmers("Parvez", "VS Code")
Atif.getInfo()
Parvez.getInfo()