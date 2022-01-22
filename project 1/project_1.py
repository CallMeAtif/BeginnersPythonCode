import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print("Comp's Turn: Snake(s) water(w) or gun(g)?")
randno = random.randint(1, 3)

if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 3:
    comp = "g"

you = input("Your Turn: Snake(s) water(w) or gun(g)?")

print(f"Comp chose {comp}")
print(f"You chose {you}")

a = gameWin(comp, you)

if comp == you:
    print("This is a tie")
elif a:
    print("You Win")
else:
    print("You Lose")    