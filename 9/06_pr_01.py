# f = open("poems.txt")
# a = f.read()
# if a.find("twinkle"):
#     print(True)
# else:
#     print(False)
# f.close()

f = open("poems.txt")
a = f.read()
if "twinkle" in a:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
