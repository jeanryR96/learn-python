# Control flow statement

firstInput = input("Enter here your first input: ")  # Input data from user
secondInput = input("Enter here your second input: ")

result = (float(firstInput) * float(secondInput))
if result > 10:
    print("Result of ", firstInput, " x ",
          secondInput, " = ", result, "\nGrade is A")
