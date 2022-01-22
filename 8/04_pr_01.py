def greatest(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return str(num1) + " is the greatest"
        else: 
            return str(num3) + " is the greatest"
    else:
        if (num2 > num3):
            return str(num2) + " is the greatest"
        else:
            return str(num3) + " is the greatest"

p = greatest(14, 16, 12)
print(p)

