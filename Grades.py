import math


class Course:
    def __init__(self, components, componentWeights):
        self.c = components
        self.w = componentWeights
        grades = []
    def calcCurrentGrade(self):
        completedAssignments = 0
        grade = 0
        fakeGrade = 0
        for i in self.components:
            print("enter the grade for {} : ", self.components[i])
            self.grades[i] = input()
            if self.grades[i] != 0
                completedAssignments++
                fakeGrade += self.componentWeights[i] * 100
            grade += self.grades[i] * self.componentWeights[i]
        print("Your current grade assuming 0s for the rest of assignments is: {}", grade)
        print("Your current grade assuming 100s for the rest of assignments is: {}", grade)




#CAP5619

#Class Attendance & Participation 10
#Programming Project I 10
#Programming Project II 10
#Homework Assignments 25
#Midterm Exam 30
#Term Project 15

#A = 93

CAP5619 = Course(["Attendance", "Project 1", "Project 2", "Homework", "Midterm, Final Project"],[.10,.10,.10,.25,.30,.15])

###################################################################

#ECO3101

#25% Canvas quizzes
#20% Midterm 1
#20% Midterm 2
#35% Final Exam

#A = 85


#################################################################

#MAC2313
# Homework 35%
# Discussion And Attendance	10%
# Exam 1 10%
# Exam 2 10%
# Exam 3 10%
# Exam 4 10%
# Final Exam 15%

#A = 93


################################################################

#MAS3015

# 20% Test 1
# 22% Test 2
# 25% Final Exam
# 15% Quiz Grade
# 18% Homework Grade

#A = 93



##########################################


courseName = input("enter a course number: ")
