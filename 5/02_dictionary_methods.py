mydict = {
    "cold": "Freezing",
    "boring": "Dull/Stupid",
    "parvez": "Good Guy",
    1: 2,
    "marks": {
        "atif": [1, 2, 3],
        "parvez": [4, 5, 6]
    },
    
}

# dictionary methods
# for printing keys present in the dictionary
print(mydict.keys())

# # prints the the (key , value) for all contents in dictionary as tuples
print(mydict.items())

# #for printing values present in the dictionary
print(list(mydict.values()))


print(mydict)
updatemydict = {
    "Aairah" : "sister",
    "Arman" : "friend",
    "boring": "stupid" # if an already existing key is entered again with a different value it changes the previous into the new value
}
mydict.update(updatemydict)#Updates the dictionary by key-values from updatemydict
print(mydict)

#returns the value of the specified key
print(mydict.get("parvez"))


print(mydict.get("parvez"))# prints value associated with key "parvez"
print(mydict["parvez"]) # prints value associated with key "parvez"

# difference between .get and [] syntax in dictionaries?
print(mydict.get("Abdullah"))# returns none as Abdullah is not present in the dictionary
print(mydict["Abdullah"]) # throws an error as Abdullah is not present in the dictionary