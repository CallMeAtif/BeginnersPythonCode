def Increment(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("Your input rsulted in a value error")

a = Increment("dfd")
print(a)