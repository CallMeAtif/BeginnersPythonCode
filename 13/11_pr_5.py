from functools import reduce
l = [5, 5, 8, 47, 6]

g = reduce(max, l)
print(g)