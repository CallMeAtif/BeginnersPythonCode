a = int(input("Enter the first Number:\n"))
b = int(input("Enter the Second Number:\n"))
c = int(input("Enter the Third Number:\n"))
d = int(input("Enter the Forth Number:\n"))

if(a > d):
    f1 = a
else:
    f1 = d

if(b > c):
    f2 = b
else:
    f2 = c

if(f1 > f2):
    print(str(f1) + " is the greatest")
else:
    print(str(f2) + " is the greatest")