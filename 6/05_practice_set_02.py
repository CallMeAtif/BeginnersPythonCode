sub1 = int(input("Enter First Subject marks:\n"))
sub2 = int(input("Enter Second Subject marks:\n"))
sub3 = int(input("Enter Third Subject marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are Failed due to less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are failed due to less percentage ")
else:
    print("Congratulatons! You have passed the exam")
