with open("this.txt") as f:
    a = f.read()

with open("this2.txt","w") as f:
    f.write(a)