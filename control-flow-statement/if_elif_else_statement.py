# Control flow with if-elif-else statement

entry = input("Input status with number: ")  # Input data from user


def if_elif_else_statement(status):
    if status == 1:
        print("Admin")
    elif status == 2:
        print("Supervisor")
    elif status == 3:
        print("Editor")
    elif status == 4:
        print("Guest")
    else:
        print("Your entry is wrong")


if_elif_else_statement(int(entry))  # data must be conver to integer type
