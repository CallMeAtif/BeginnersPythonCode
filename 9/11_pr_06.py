### USE (.lower()) to make the characters in lower case

with open("log.txt") as f:
    a = f.read()

if "python" in a.lower():
    print("Yes python is present")
else:
    print("No python is not present")