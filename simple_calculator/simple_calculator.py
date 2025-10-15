# This program is a Simple calculator, which can perform Addition, Subtraction, Multiplication, Division, remainder, exponent.


# Functions for various calculations
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    
def remainder(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return pow(num1, num2)


# Using while loop, since we don't have any fixed number of iterations.
op = True
while op:

    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

    operation = input("Enter the operation, you want to perform(+, -, *, /, **, %) :")

    if operation == '+':
        print(addition(num1, num2))

    elif operation == '-':
        print(subtraction(num1, num2))

    elif operation == '*':
        print(multiplication(num1, num2))

    elif operation == '/':
        print(division(num1, num2))

    elif operation == '%':
        print(remainder(num1, num2))

    elif operation == "**":
        print(exponent(num1, num2))

    else:
        print("Invalid operator")

    more = input("Wanna Play again? (yes/no) : ")
    # making op = False to exit the loop, if user des not want to do any more calculations
    if more.lower() == 'no':
        op = False



