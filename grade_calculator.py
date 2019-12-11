print("Calculate what you need to get on your exam")
finish = False
overallGrade = 0
gradeAcheived = 0

while finish == False:
    mark = int(input("Please input your current mark: "))
    worth = int(input('How much % is that worth:  '))
    overallGrade += mark * worth/100
    gradeAcheived += worth
    valid = False

    while valid == False:
        done = str(input("Do you have any more marks? y/n "))
        if done == 'Y' or done =='y' or done =='Yes' or done =='yes':
            finish = False
            valid = True
        elif done == 'N' or done == 'n' or done == 'no' or done == 'No':
            finish = True
            valid = True
        else:
            valid = False
            print("invalid response, please try again")

targetMark = int(input("What is your target overall grade? "))
examWorth = 100 - gradeAcheived

examMark = round((targetMark - overallGrade) / (examWorth/100))
if examMark > 100:
    highestMark = overallGrade + examWorth
    print("Sorry that is not possible. The highest mark you can acheive is ", highestMark, " if you recieve perfect on the exam.")
elif examMark < 0:
    print("Even if you do not write the exam, you will still get ", overallGrade)
else:
    print("You need to get a ",examMark, "on the final exam")

