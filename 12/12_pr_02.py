a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for index, item in enumerate(a):
    if index == 2 or index == 4 or index == 6:
        b.append(item)

print(b)
