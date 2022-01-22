def sumof(n):
    if n==1 or n==0:
        return 1
    return sumof(n-1) + n

p = sumof(5)
print(p)