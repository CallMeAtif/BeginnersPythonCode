def openfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"File is not found '{filename}'") 


openfile("1.txt")
openfile("2.txt")
openfile("3.txt")