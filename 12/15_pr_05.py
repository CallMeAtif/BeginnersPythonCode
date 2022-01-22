n = int(input("Enter a Number:\n"))

table = [n*i for i in range(1,11)]
g = str(table)

with open("tables.txt", "w") as f:
    a = f.write(g)