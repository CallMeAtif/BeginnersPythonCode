# with (with) statement there is no need to close file as its done automatically 
with open("another.txt",) as f:
    a = f.read()
    print(a)
    
with open("another.txt","w") as t:
    a = t.write("Hello")
    print(a)
    