class Sample:
    a = "Atif"

obj = Sample()
obj.a = "Parvez" #this creates an instance attribute
# Sample.a = "Parvez" # this changes class attribute
print(Sample.a)
print(obj.a)
