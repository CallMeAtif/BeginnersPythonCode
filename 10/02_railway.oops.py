class RailwayForm():
    Formtype = "Railwayform"
    def printData(self):
        print(f"The applicant's name is {self.name}")
        print(f"The train name is {self.train}")

atifapplication = RailwayForm()
atifapplication.name = "Atif"
atifapplication.train = "Rajdhani Express"
atifapplication.printData()
print(atifapplication.Formtype)