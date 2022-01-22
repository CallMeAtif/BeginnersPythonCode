try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)

except ValueError as e:
    print(f"Your input resulted in value error")

except ZeroDivisionError as z:
    print("Your input resulted a ZeroDivisionError")
    