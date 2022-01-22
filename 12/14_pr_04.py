a = int(input("Enter a number:\n"))
b = int(input("Enter a number:\n"))

try:
    a = a/b
    print(a)

except ZeroDivisionError as z:
    print("Infinite")