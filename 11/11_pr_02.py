class Animals():
    animalType = "mammals"
    
class Pets(Animals):
    color = "black"
    
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
print(d.animalType)
print(d.color)
d.bark()