l = [5,10,15,42,78,96,45,36,90,85,39]
dby5 = lambda a: a%5==0

g = list(filter(dby5, l))
print(g)