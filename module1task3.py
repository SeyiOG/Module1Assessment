#Zenith Crest Academy (ZCA) Grading System


#import random
#nubanaccts = (random.sample(range(1000000000, 2999999999), 1000)) #generate the list of account numbers
firstname = input("enter your firstname: ") #user enters firstname 
middlename = input("enter your middlename: ") #user enters middlename
lastname = input("enter your lastname: ") #user enters lastname
userdetails = [firstname, middlename, lastname] #create the userdetails list
#retrieve the customer details from the userdetails list
studentname = "Student Name: " + userdetails[2].upper()+','+' '+userdetails[0].capitalize()+' '+userdetails[1][0].upper()+'.' #format student name
courses = ["1. DB", "2. INTRO TO PROGRAMMING", "3. OOP", "4. WEB PROGRAMMING"] #create list of all courses taken by students


score1 = int(input("%s score is: "%(courses[0]))) #input student's score in the first course
if (score1 >= 50):                                #if score is greater or equal to 50
    print("You can take the next course")         #display message as shown
    score2 = int(input("%s score is: "%(courses[1]))) #input student's score in the second course
    if (score2 >= 50):                              #if score is greater or equal to 50
        print("You can take the next course")         #display message as shown
        score3 = int(input("%s score is: "%(courses[2]))) #input student's score in the third course
        if (score3 >= 50):                              #if score is greater or equal to 50
            print("You can take the next course")         #display message as shown
            score4 = int(input("%s score is: "%(courses[3]))) #input student's score in the fourth course
            totalscore = int(score1 + score2 + score3 + score4)    #calculate student's total score
            if (totalscore >= 300):                              #if total score is greater or equal to 300
                print("Congratulations! You have passed.\nKeep up the good work!") #display message as shown
            elif (totalscore < 300):
                print("please retake the assessment")
        elif (score3 < 50):
            print("You cannot take the next course")             #display message as shown
            score4 = -1                                #Autoassign score of i-1 to the outstanding courses
    elif (score2 < 50):
        print("You cannot take the next course")             #display message as shown
        score4 = -1 ; score3 = -1        #Autoassign score of i-1 to the outstanding courses
else:
    print("You cannot take the next course")                 #display message as shown
    score4 = -1 ; score3 = -1 ; score2 = -1 #Autoassign score of -1 to the outstanding courses

#Design Grading System

grade1 = str()                             #declare the first grade
if (score1 >= 70):                         #if score greater or equal to 70, assign grade A
    grade1 = "A"
elif (score1 >= 60) and (score1 <= 69):    #if score is from 60-69, assign grade B
    grade1 = "B"
elif (score1 >= 50) and (score1 <= 59):    #if score is from 50-59, assign grade C
    grade1 = "C"
elif (score1 >= 40) and (score1 <= 49):    #if score is from 40-49, assign grade D
    grade1 = "D"
elif (score1 < 40):                          #if score less than 40, assign grade F
    grade1 = "F"
else:                                      #if score is less than 40, assign grade incomplete
    grade1 = "Incomplete"

grade2 = str()                             #declare the second grade
if (score2 >= 70):                         #if score greater or equal to 70, assign grade A
    grade2 = "A"
elif (score2 >= 60) and (score2 <= 69):    #if score is from 60-69, assign grade B
    grade2 = "B"
elif (score2 >= 50) and (score2 <= 59):    #if score is from 50-59, assign grade C
    grade2 = "C"
elif (score2 >= 40) and (score2 <= 49):    #if score is from 40-49, assign grade D
    grade2 = "D"
elif (score2 < 40):                          #if score less than 40, assign grade F
    grade2 = "F"
else:                                      #if score is less than 40, assign grade incomplete
    grade2 = "Incomplete"

grade3 = str()                             #declare the third grade
if (score3 >= 70):                         #if score greater or equal to 70, assign grade A
    grade3 = "A"
elif (score3 >= 60) and (score3 <= 69):    #if score is from 60-69, assign grade B
    grade3 = "B"
elif (score3 >= 50) and (score3 <= 59):    #if score is from 50-59, assign grade C
    grade3 = "C"
elif (score3 >= 40) and (score3 <= 49):    #if score is from 40-49, assign grade D
    grade3 = "D"
elif (score3 < 40):                          #if score less than 40, assign grade F
    grade3 = "F"
else:                                      #if score is less than 40, assign grade incomplete
    grade3 = "Incomplete"

grade4 = str()                             #declare the fourth grade
if (score4 >= 70):                         #if score greater or equal to 70, assign grade A
    grade4 = "A"
elif (score4 >= 60) and (score4 <= 69):    #if score is from 60-69, assign grade B
    grade4 = "B"
elif (score4 >= 50) and (score4 <= 59):    #if score is from 50-59, assign grade C
    grade4 = "C"
elif (score4 >= 40) and (score4 <= 49):    #if score is from 40-49, assign grade D
    grade4 = "D"
elif (score4 < 40):                          #if score less than 40, assign grade F
    grade4 = "F"
else:                                      #if score is less than 40, assign grade incomplete
    grade4 = "Incomplete"

gradelist = [grade1, grade2, grade3, grade4]

if ((score1 + score2 + score3 + score4) >= 300):                              #if total score is greater or equal to 300
    assessment = "Congratulations! You have passed.\nKeep up the good work!" #assessment is string message as shown
elif ((score1 + score2 + score3 + score4) < 300):                           #if total score is less than 300
    assessment = "Minimum Total Score not met. Retake The Assessment"       #assessment is string message as shown

ass2file = open("mod1task3out.txt", "w+") #open mod1task3out text file
#write the student name, course list and grade list to a text file
ass2file.write("ZCA Results Slip\n%s\nCourse List: %s\nGrade List: %s\n%s"%(studentname,courses,gradelist,assessment))
#display the student name, course list and grade list on terminal
print("ZCA Results Slip\n%s\nCourse List: %s\nGrade List: %s\n%s"%(studentname,courses,gradelist,assessment)) 

