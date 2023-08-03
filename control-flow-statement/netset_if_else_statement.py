# Control flow with nested if-else statement

courseOne = int(input("Input number of course one: "))
courseSecond = int(input("Input number of course Second: "))

if courseOne >= courseSecond:
    if courseOne >= courseSecond:
        print(courseOne, "is greater than ", courseSecond)
    else:
        print(courseOne, "is equal to ", courseSecond)
elif courseSecond >= courseOne:
    if courseSecond == courseOne:
        print(courseSecond, " is equal to ", courseOne)
    else:
        print(courseSecond, " is greater than ", courseOne)
else:
    print(courseOne, "is smaller than ", courseSecond)
