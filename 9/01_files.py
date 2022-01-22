# use open function to read the content of a file
# f = open("sample.txt", "r")
f = open("sample.txt")#by deafult the mode is r(Read)
# data = f.read()
data = f.read(6)#reads first 6 characters from the file file
print(data)
f.close()