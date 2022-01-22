def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "       Parvez is a not good boy"
a = remove_and_strip(this, " not")
print(a)

# print(this)
# print(this.strip())