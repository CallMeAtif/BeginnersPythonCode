a = [2 , 45, 78, 30, 95, 120, 77, 15, 76]

# b = []
# for item in list1:
#     if item%2==0:
#         b.append(item)

b = [i for i in a if i%2==0]

print(b)

