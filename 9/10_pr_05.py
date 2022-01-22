words = ["kaddu","bad", "dumb", "donkey"]

with open("sample.txt") as f:
    a = f.read()

for word in words:    
    a = a.replace(word, "$$@^*#*&$")

with open("sample.txt","w") as f:
    f.write(a)