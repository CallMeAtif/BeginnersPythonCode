import os

a = "rename_me.txt"
b = "renamed_by_python.txt"

with open(a) as f:
    content = f.read()

with open(b, "w") as f:
    f.write(content)

os.remove(a)