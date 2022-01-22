# b = set()
# print(type(b))

# # Adding an element in an empty set
# b.add(4)
# b.add(4)
# b.add(5)
# b.add(5)
# b.add(5)
# # b.add([4, 5, 6]) #cannot add list or dictionary in sets
# b.add((4, 5, 6))  # can use tuple in sets

# print(b)

# # lenght of this set
# print(len(b))  # print the lenght of this set

# # removal of an item from the element
# b.remove(5)  # removes the element from the set b
# # b.remove(15)# throws an error while removing 15 (whhich is not present in the set b
# print(b)

# # removes any random element from the set
# print(b.pop())

# # it makes the set empty
# print(b.clear())

e = {1, 2, 3, 5, 7}
d = {1, 2, 3, 4, 6}

print(e.union(d))#returns a new set with all the content from both sets

q = {1, 2, 3, 5, 7}
p = {1, 2, 3, 4, 6}

print(q.intersection(p))# returns a set which contains items from both sets