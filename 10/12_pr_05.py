class Train():
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The number of seats in this train is {self.seats}")

    def getFareInfo(self):
        print(f"The fare of this train is Rs {self.fare}")

    def getTicket(self):
        if(self.seats>0):
            print(f"YOORAH!  Your ticket is booked, Your seat no. is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full, kindly try Another train")

Rajdhani = Train("Rajdhani Express : 120562", 2, 100)
Rajdhani.getFareInfo()
Rajdhani.getTicket()
Rajdhani.getStatus()