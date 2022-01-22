a = int(input("Enter the number:\n"))

factorial = 1
for i in range(1, a+1):
    factorial *= i
print(f"The factorial of {a} is {factorial}")