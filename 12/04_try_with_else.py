try:
    i = int(input("Enter a number: "))
    a = 1/i

except Exception as e:
    print(f"Some error occurred {e}")

else:
    print("We were successful")