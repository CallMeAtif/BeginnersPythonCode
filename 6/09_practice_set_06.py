marks =  int(input("Enter your marks:\n"))

if(marks >= 90 and marks<=100):
    grade ="Excellent"
elif (marks>100):
    print("Please enter a valid marks")
    grade = "None"
elif(marks >= 80):
    grade = "A"
elif(marks >= 70):
    grade= "B"
elif(marks >= 60):
    grade= "C"
elif(marks >= 50):
    grade = "D"
else:
    grade = "Fail"

print("Your grade is:\n" + grade)