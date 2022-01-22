name = input("Enter your name:\n")
marks = int(input("Enter your marks:\n"))
number = int(input("Enter your number:\n"))

# info = "The name of the student is {},His marks are {} and his number is {}".format(name,marks,number)
                                # OR
info = "The name of the student is {},His marks are {} and his number is {}"

output = info.format(name,marks,number)
print(output)