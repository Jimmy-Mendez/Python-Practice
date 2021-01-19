
class Course:
    
    def __init__(self, name, components, componentWeights):
        self.n = name
        self.c = components
        self.w = componentWeights

    def calcCurrentGrade(self):
        count = 0
        grades = []
        completedAssignments = 0
        grade = 0.0
        fakeGrade = 0
        points_lost = 0
        for i in self.c:
            print("enter the grade for: ", i)
            grades.append(float(input()))
            if grades[count] != 0:
                completedAssignments+=1
                points_lost += (self.w[count] * 100)-(grades[count] * self.w[count])
            else:
                fakeGrade += self.w[count] * 100
            grade += grades[count] * self.w[count]
            count+=1
        fakeGrade = fakeGrade + grade
        print("Your current grade assuming 0s for the rest of assignments is: ", grade)
        print("Your current grade assuming 100s for the rest of assignments is: ", fakeGrade)
        print("points lost so far:", points_lost)




#CAP5619

#Class Attendance & Participation 10
#Programming Project I 10
#Programming Project II 10
#Homework Assignments 25
#Midterm Exam 30
#Term Project 15

#A = 93

CAP5619 = Course("CAP 5619", ["Attendance", "Project 1", "Project 2", "Homework", "Midterm", "Final Project"],[.10,.10,.10,.25,.30,.15])

###################################################################

#ECO3101

#25% Canvas quizzes
#20% Midterm 1
#20% Midterm 2
#35% Final Exam

#A = 85

ECO3101 = Course("ECO 3101", ["Quizzes", "Midterm 1", "Midterm 2", "Final"],[.25,.20,.20,.35])


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

MAC2313 = Course("MAC 2313", ["Homework", "Discussions", "Exam 1", "Exam 2", "Exam 3", "Exam 4", "Final"],[.35,.10,.10,.10,.10,.10,.15])

################################################################

#MAS3015

# 20% Test 1
# 22% Test 2
# 25% Final Exam
# 15% Quiz Grade
# 18% Homework Grade

#A = 93

MAS3105 = Course("MAS 3105", ["Homework", "Quizzes", "Test 1", "Test 2", "Final"],[.18,.15,.20,.22,.25])

##########################################


CourseList = [CAP5619, ECO3101, MAC2313, MAS3105]

courseName = input("enter a course number: ")

course = Course("N/A",[],[])

for i in CourseList:
    if courseName == i.n:
        course = i

course.calcCurrentGrade()
