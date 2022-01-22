# Creatingg a dictionary with {}
# mydict = {
#     "fast" : "In a speedy manner",
#     "Atif" : "name",
#     "Parvez" : "Uncle",
#     "Marks" : [1, 2, 3],
#     "Anotherdict" : {'Atif' : 'Player'}
# }
# # print(mydict["fast"])
# # print(mydict["Atif"])
# # print(mydict["Parvez"])
# mydict["Marks"] = [16, 3, 25]
# print(mydict["Marks"])
# print(mydict["Anotherdict"]["Atif"])
mydict2 = {
    "Cold" : "Freezing\n",
    "Boring" : "Dull/Stupid",
    "Parvez" : "Good Guy",
    "Marks" : {
        "Atif" : [1, 2, 3],
        "Parvez" : [4, 5, 6]
    }
}
print(mydict2["Parvez"])
mydict2["Marks"]["Parvez"]=[10, 10, 10]
print(mydict2["Marks"]["Parvez"])
mydict2["Marks"]["Atif"] ="Atif"
print(mydict2["Marks"]["Atif"])
print(mydict2)