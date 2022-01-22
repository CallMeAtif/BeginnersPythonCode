class Number():
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num

n1 = Number(6)
n2 = Number(4)

sum = n1 + n2
print(sum)
