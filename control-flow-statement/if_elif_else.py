# Control flow statement 'if-elif-else'

course = input("Enter here your course 1: ")  # Input data from user

firstCourse = int(course)
if firstCourse >= 95:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: A")
elif firstCourse >= 90:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: A-")
elif firstCourse >= 85:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: B+")
elif firstCourse >= 80:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: B")
elif firstCourse >= 75:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: B-")
elif firstCourse >= 70:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: C+")
elif firstCourse >= 65:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: C")
elif firstCourse >= 60:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: C-")
else:
    print("Result of Course 1 = ", firstCourse, "\nGrade is: F = 'Failed'")
