text = input("Enter the text:\n")

if("click this" in text):
    spam = True
elif("watch this" in text):
    spam = True
elif("subscribe now" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam")
else:
    print("This is not a spam")