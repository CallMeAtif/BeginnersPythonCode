# 1st solution

mydict = {
    "dabba": "Box",
    "Pankha": "Fan",
    "bhagna": "Run",
    "khelna": "Play"
}
print("options are ",mydict.keys())
a = input("Enter the word:\n")
#this will throw an error if the key is not present in the dictionary
# print("The meaning of your word is:",mydict[a])
#below line will not throw an error
print("The meaning of your word is:",mydict.get(a))